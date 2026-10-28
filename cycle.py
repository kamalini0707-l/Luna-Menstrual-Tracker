
from datetime import date, timedelta
import database


def get_cycle_lengths():
    periods = database.get_periods()
    starts = []

    for period in periods:
        starts.append(date.fromisoformat(period[1]))

    starts.sort()

    lengths = []

    for i in range(1, len(starts)):
        days = (starts[i] - starts[i - 1]).days

        if days > 0:
            lengths.append(days)

    return lengths


def get_next_period():
    periods = database.get_periods()

    if len(periods) < 2:
        return None, None

    lengths = get_cycle_lengths()

    if len(lengths) == 0:
        return None, None

    recent_lengths = lengths[-6:]
    avg_length = round(sum(recent_lengths) / len(recent_lengths))

    latest_start = date.fromisoformat(periods[0][1])
    next_date = latest_start + timedelta(days=avg_length)

    return next_date, avg_length


def get_prediction_message():
    next_date, avg_length = get_next_period()

    if next_date is None:
        return "Record at least two period start dates to get an estimate."

    today = date.today()
    days_left = (next_date - today).days

    if days_left < 0:
        return (
            f"Your estimated date was {abs(days_left)} days ago. "
            "Cycles can vary, so this estimate may not match your actual period."
        )

    if days_left == 0:
        return "Your period is estimated to start today."

    if days_left <= 3:
        return f"Your period may start in about {days_left} day(s)."

    return f"Your next period is estimated in about {days_left} days."
