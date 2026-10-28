import sqlite3
import hashlib
import hmac
import secrets
import re
from contextvars import ContextVar
from datetime import date

DB_NAME = "luna.db"
_current_user_id = ContextVar("luna_user_id", default=None)


def set_current_user(user_id):
    """Set the account for this Streamlit script run (session-local context)."""
    _current_user_id.set(int(user_id))


def _uid():
    uid = _current_user_id.get()
    if uid is None:
        raise RuntimeError("Please log in before accessing Luna data.")
    return int(uid)


def connect():
    con = sqlite3.connect(DB_NAME, timeout=15)
    con.execute("PRAGMA foreign_keys = ON")

    # Preserve older tables that were created before account support.
    tables = {row[0] for row in con.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()}

    if "periods" in tables:
        cols = {row[1] for row in con.execute("PRAGMA table_info(periods)").fetchall()}
        if "user_id" not in cols:
            old_name = "periods_legacy"
            suffix = 1
            while old_name in tables:
                old_name = f"periods_legacy_{suffix}"
                suffix += 1
            con.execute(f"ALTER TABLE periods RENAME TO {old_name}")
            tables.add(old_name)

    if "daily_logs" in tables:
        cols = {row[1] for row in con.execute("PRAGMA table_info(daily_logs)").fetchall()}
        if "user_id" not in cols:
            old_name = "daily_logs_legacy"
            suffix = 1
            while old_name in tables:
                old_name = f"daily_logs_legacy_{suffix}"
                suffix += 1
            con.execute(f"ALTER TABLE daily_logs RENAME TO {old_name}")
            tables.add(old_name)

    con.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL COLLATE NOCASE UNIQUE,
        email TEXT NOT NULL COLLATE NOCASE UNIQUE,
        password_hash TEXT NOT NULL,
        password_salt TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )""")
    con.execute("""CREATE TABLE IF NOT EXISTS periods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL
    )""")
    con.execute("""CREATE TABLE IF NOT EXISTS daily_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        log_date TEXT NOT NULL,
        mood TEXT NOT NULL,
        energy INTEGER NOT NULL,
        symptoms TEXT,
        notes TEXT,
        UNIQUE(user_id, log_date)
    )""")
    con.commit()
    return con


def _password_hash(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 310000).hex()


def register_user(username, email, password):
    username, email = username.strip(), email.strip().lower()
    if not re.fullmatch(r"[A-Za-z0-9_.-]{3,30}", username):
        return False, "Please choose a valid username."
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return False, "Please enter a valid email address."
    if len(password) < 10:
        return False, "Password must contain at least 10 characters."
    salt = secrets.token_bytes(16)
    digest = _password_hash(password, salt)
    con = connect()
    try:
        con.execute("INSERT INTO users(username,email,password_hash,password_salt) VALUES(?,?,?,?)",
                    (username, email, digest, salt.hex()))
        con.commit()
        return True, "Account created."
    except sqlite3.IntegrityError:
        return False, "That username or email is already registered."
    finally:
        con.close()


def login_user(username_or_email, password):
    con = connect()
    row = con.execute("""SELECT id, username, password_hash, password_salt
        FROM users WHERE username = ? COLLATE NOCASE OR email = ? COLLATE NOCASE""",
        (username_or_email.strip(), username_or_email.strip())).fetchone()
    con.close()
    if not row:
        return None
    try:
        expected = _password_hash(password, bytes.fromhex(row[3]))
    except (ValueError, TypeError):
        return None
    if hmac.compare_digest(expected, row[2]):
        return row[0], row[1]
    return None


def get_user_email():
    con = connect()
    row = con.execute("SELECT email FROM users WHERE id=?", (_uid(),)).fetchone()
    con.close()
    return row[0] if row else None


def add_period(start_date, end_date):
    con = connect()
    con.execute("INSERT INTO periods(user_id,start_date,end_date) VALUES(?,?,?)", (_uid(), start_date, end_date))
    con.commit(); con.close()


def get_periods():
    con = connect()
    rows = con.execute("SELECT id,start_date,end_date FROM periods WHERE user_id=? ORDER BY start_date DESC", (_uid(),)).fetchall()
    con.close(); return rows


def delete_period(period_id):
    con = connect(); con.execute("DELETE FROM periods WHERE id=? AND user_id=?", (period_id, _uid())); con.commit(); con.close()


def create_daily_table():
    con = connect(); con.close()


def save_daily_log(log_date, mood, energy, symptoms, notes):
    con = connect()
    con.execute("""INSERT INTO daily_logs(user_id,log_date,mood,energy,symptoms,notes)
        VALUES(?,?,?,?,?,?) ON CONFLICT(user_id,log_date) DO UPDATE SET
        mood=excluded.mood, energy=excluded.energy, symptoms=excluded.symptoms, notes=excluded.notes""",
        (_uid(), log_date, mood, energy, symptoms, notes))
    con.commit(); con.close()


def get_daily_logs():
    con = connect()
    rows = con.execute("SELECT id,log_date,mood,energy,symptoms,notes FROM daily_logs WHERE user_id=? ORDER BY log_date DESC", (_uid(),)).fetchall()
    con.close(); return rows


def delete_daily_log(log_id):
    con = connect(); con.execute("DELETE FROM daily_logs WHERE id=? AND user_id=?", (log_id, _uid())); con.commit(); con.close()


def export_all_data():
    con = connect(); uid = _uid()
    periods = con.execute("SELECT start_date,end_date FROM periods WHERE user_id=? ORDER BY start_date", (uid,)).fetchall()
    logs = con.execute("SELECT log_date,mood,energy,symptoms,notes FROM daily_logs WHERE user_id=? ORDER BY log_date", (uid,)).fetchall()
    con.close(); return periods, logs


def delete_all_data():
    con = connect(); uid = _uid()
    con.execute("DELETE FROM periods WHERE user_id=?", (uid,))
    con.execute("DELETE FROM daily_logs WHERE user_id=?", (uid,))
    con.commit(); con.close()


def get_data_counts():
    con = connect(); uid = _uid()
    p = con.execute("SELECT COUNT(*) FROM periods WHERE user_id=?", (uid,)).fetchone()[0]
    d = con.execute("SELECT COUNT(*) FROM daily_logs WHERE user_id=?", (uid,)).fetchone()[0]
    con.close(); return p, d


def validate_period(start_date, end_date):
    start, end = date.fromisoformat(start_date), date.fromisoformat(end_date)
    if start > date.today(): return False, "Period start date cannot be in the future."
    if end > date.today(): return False, "Period end date cannot be in the future."
    if end < start: return False, "End date cannot be before start date."
    if (end - start).days + 1 > 15: return False, "Please check the dates: the period duration is unusually long."
    for period in get_periods():
        old_start, old_end = date.fromisoformat(period[1]), date.fromisoformat(period[2])
        if start == old_start and end == old_end: return False, "This period record already exists."
        if start <= old_end and end >= old_start: return False, "This period overlaps an existing record."
    return True, ""
