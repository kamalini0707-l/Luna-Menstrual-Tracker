
import streamlit as st
from datetime import date
import database
import cycle
import analytics
import pandas as pd
import reminders
st.set_page_config(
    page_title="Luna | Cycle & Wellness",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

.stApp {
    background-color: #FAF7FC;
    color: #40364A;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background-color: #F0E8F7;
}

[data-testid="stSidebar"] h1 {
    color: #755B89 !important;
}

h1, h2, h3 {
    color: #493653 !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
}

p, label, [data-testid="stCaptionContainer"] {
    color: #62566B;
    font-family: 'Inter', sans-serif;
    font-size: 16px;
}

div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #E8DDED;
    padding: 18px;
    border-radius: 16px;
}

[data-testid="stMetricLabel"] {
    color: #62566B !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #493653 !important;
    font-size: 32px !important;
    font-weight: 800 !important;
}

div.stButton > button,
[data-testid="stFormSubmitButton"] > button {
    background-color: #89699F !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 8px 18px;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
}

div.stButton > button:hover,
[data-testid="stFormSubmitButton"] > button:hover {
    background-color: #755B89 !important;
    color: #FFFFFF !important;
}

div.stButton > button p,
[data-testid="stFormSubmitButton"] button p {
    color: #FFFFFF !important;
}

div[data-testid="stForm"] {
    background-color: #FFFFFF;
    border: 1px solid #E8DDED;
    padding: 20px;
    border-radius: 16px;
}

input, textarea {
    color: #40364A !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] {
    background: #FFFFFF !important;
    border-radius: 10px !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stSelectbox"] [data-baseweb="select"] > div > div {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border-color: #DCCBE8 !important;
    box-shadow: none !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] * {
    font-family: 'Nunito', sans-serif !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] span,
[data-testid="stSelectbox"] [data-baseweb="select"] input {
    color: #493653 !important;
    -webkit-text-fill-color: #493653 !important;
    font-size: 16px !important;
    font-weight: 700 !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[role="listbox"] {
    background-color: #FFFFFF !important;
    color: #493653 !important;
}

[role="option"] {
    background-color: #FFFFFF !important;
    color: #493653 !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 16px !important;
}

[role="option"]:hover,
[role="option"][aria-selected="true"] {
    background-color: #F0E8F7 !important;
}

[data-testid="stDateInput"] input {
    background-color: #FFFFFF !important;
    color: #493653 !important;
    -webkit-text-fill-color: #493653 !important;
    border: 1px solid #DCCBE8 !important;
    border-radius: 10px !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

[data-testid="stDateInput"] button {
    color: #755B89 !important;
}

[data-testid="stSlider"] [role="slider"] {
    background-color: #89699F !important;
    border-color: #89699F !important;
}

[data-testid="stWidgetLabel"] p {
    color: #62566B !important;
    font-weight: 500 !important;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #F4EDF9 !important;
    border: 1px solid #E8DDED !important;
    border-radius: 20px !important;
    padding: 12px !important;
}

[data-testid="stMarkdownContainer"] h3 {
    color: #493653 !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 27px !important;
    font-weight: 800 !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #62566B !important;
}

[data-testid="stDateInput"] input {
    background-color: #F0E8F7 !important;
    color: #493653 !important;
    -webkit-text-fill-color: #493653 !important;
    border: 1px solid #E8DDED !important;
    border-radius: 12px !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    min-height: 48px !important;
}

[data-testid="stDateInput"] button {
    color: #755B89 !important;
    background-color: transparent !important;
}

[data-testid="stForm"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E8DDED !important;
    border-radius: 20px !important;
    padding: 24px !important;
}

[data-testid="stFormSubmitButton"] button {
    background-color: #89699F !important;
    color: #FFFFFF !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    padding: 10px 22px !important;
}

[data-testid="stFormSubmitButton"] button p {
    color: #FFFFFF !important;
}

[data-testid="stFormSubmitButton"] button:hover {
    background-color: #755B89 !important;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #F0E8F7;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2 {
    color: #755B89 !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 30px !important;
    font-weight: 800 !important;
    margin: 0 0 24px 0 !important;
}

[data-testid="stSidebar"] .luna-section-label {
    color: #95829F;
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin: 0 0 10px 0;
}

[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background-color: transparent !important;
    color: #62566B !important;
    border: 1px solid transparent !important;
    border-radius: 12px !important;
    padding: 10px 12px !important;
    min-height: 44px;
    font-family: 'Nunito', sans-serif !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    box-shadow: none !important;
    transition: background-color 0.15s ease;
}

[data-testid="stSidebar"] div.stButton > button:hover {
    background-color: #E7DAF0 !important;
    color: #654779 !important;
    border-color: transparent !important;
}

[data-testid="stSidebar"] div.stButton > button p {
    color: inherit !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 15px !important;
    font-weight: inherit !important;
}

[data-testid="stSidebar"] div.stButton > button[kind="primary"],
[data-testid="stSidebar"] div.stButton > button[data-testid="stBaseButton-primary"] {
    background-color: #E2D2ED !important;
    color: #654779 !important;
    border-color: #D7C2E5 !important;
    font-weight: 800 !important;
}

[data-testid="stSidebar"] div.stButton > button[kind="primary"] p,
[data-testid="stSidebar"] div.stButton > button[data-testid="stBaseButton-primary"] p {
    color: #654779 !important;
    font-weight: 800 !important;
}
</style>
<div class="luna-section-label">YOUR SPACE</div>
""", unsafe_allow_html=True)

# Account access: keep the existing Luna theme and custom navigation.
if "user_id" not in st.session_state:
    st.session_state.user_id = None
    st.session_state.username = None

if st.session_state.user_id is None:
    st.markdown("<div style='text-align:center; padding-top:3rem;'><h1>🌙 Luna</h1><p>Your cycle, your space.</p></div>", unsafe_allow_html=True)
    left, center, right = st.columns([1, 1.2, 1])
    with center:
        mode = st.radio("", ["Log in", "Create account"], horizontal=True, label_visibility="collapsed")
        if mode == "Create account":
            with st.form("create_account_form"):
                new_username = st.text_input("Username", max_chars=30)
                new_email = st.text_input("Email address")
                new_password = st.text_input("Password (at least 10 characters)", type="password")
                confirm_password = st.text_input("Confirm password", type="password")
                create_clicked = st.form_submit_button("Create account", use_container_width=True)
            if create_clicked:
                if new_password != confirm_password:
                    st.error("The passwords do not match.")
                else:
                    ok, message = database.register_user(new_username, new_email, new_password)
                    if ok:
                        st.success("Account created. Please log in.")
                    else:
                        st.error(message)
        else:
            with st.form("login_form"):
                login_name = st.text_input("Username or email")
                login_password = st.text_input("Password", type="password")
                login_clicked = st.form_submit_button("Log in", use_container_width=True)
            if login_clicked:
                account = database.login_user(login_name, login_password)
                if account:
                    st.session_state.user_id = account[0]
                    st.session_state.username = account[1]
                    st.rerun()
                else:
                    st.error("The username/email or password is incorrect.")
    st.stop()

# All database calls on this run now use the signed-in account.
database.set_current_user(st.session_state.user_id)

st.sidebar.markdown("## 🌙 Luna")
st.sidebar.caption(f"Signed in as {st.session_state.username}")
if st.sidebar.button("Log out", use_container_width=True):
    st.session_state.user_id = None
    st.session_state.username = None
    st.session_state.page = "Home"
    st.rerun()

if "page" not in st.session_state:
    st.session_state.page = "Home"

navigation = [
    ("⌂", "Home"),
    ("🌸", "Period Calendar"),
    ("♡", "Daily Journal"),
    ("✧", "Insights"),
    ("⚙", "Settings")
]

for symbol, name in navigation:
    button_type = "primary" if st.session_state.page == name else "secondary"
    if st.sidebar.button(
        f"{symbol}   {name}",
        key=f"nav_{name}",
        use_container_width=True,
        type=button_type
    ):
        st.session_state.page = name
        st.rerun()

page = st.session_state.page


if page == "Home":

    st.title("Your little corner of calm 🌷")
    st.write("Understand your cycle. Listen to your body. Take care of yourself.")
    st.caption(date.today().strftime("%A, %d %B %Y"))

    st.write("")

    
    next_date, avg_length = cycle.get_next_period()
    periods = database.get_periods()

    col1, col2, col3 = st.columns(3)

    
    with col1:
        periods = database.get_periods()
        today = date.today()

        past_periods = [
            p for p in periods
            if date.fromisoformat(p[1]) <= today
        ]

        if past_periods:
            latest_start = max(
                date.fromisoformat(p[1])
                for p in past_periods
            )

            cycle_day = (today - latest_start).days + 1

            st.metric("🌸 Current Cycle Day", cycle_day)
        else:
            st.metric("🌸 Current Cycle Day", "Not available")

        st.caption("Counted from the latest recorded period start date.")

    with col2:
        if next_date is not None:
            st.metric(
                "🩷 Estimated Next Period",
                next_date.strftime("%d %b %Y")
            )
            st.caption(f"Average cycle length: {avg_length} days")
        else:
            st.metric("🩷 Estimated Next Period", "Not available")
            st.caption("Record at least two period start dates.")

    with col3:
        st.metric("✨ Daily Check-in", "Ready")
        st.caption("Record how you're feeling today.")

    st.write("")
    st.divider()

    st.subheader("A moment for yourself ☁️")
    st.write("A small check-in can help you notice patterns over time.")

    with st.form("daily_checkin"):
        mood = st.selectbox(
            "How are you feeling today?",
            ["Choose a mood", "Happy", "Calm", "Anxious",
             "Sad", "Irritated", "Tired"]
        )

        energy = st.slider(
            "Your energy level",
            min_value=1,
            max_value=5,
            value=3
        )

        submitted = st.form_submit_button("Save check-in")

        if submitted:
            if mood == "Choose a mood":
                st.warning("Please choose a mood first.")
            else:
                st.success(
                    f"Check-in recorded for this session: {mood}, "
                    f"energy level {energy}/5."
                )

    st.write("")
    st.info(
        "Luna provides estimates based on recorded cycle history. "
        "These are not medical predictions."
    )
    st.divider()
    reminders.show_reminder()

elif page == "Period Calendar":
    st.title("🌸 Period Calendar")
    st.write("Record and view your period history.")

    st.subheader("Add a period")

    with st.form("period_form"):
        start_date = st.date_input("Period start date", value=None)
        end_date = st.date_input("Period end date", value=None)

        submitted = st.form_submit_button("Save period")
        
        if submitted:
            valid, message = database.validate_period(
                start_date.isoformat(),
                end_date.isoformat()
            )

            if valid:
                database.add_period(
                    start_date.isoformat(),
                    end_date.isoformat()
                )
                st.success("Period record saved!")
                st.rerun()
            else:
                st.error(message)

    st.divider()
    st.subheader("Your period history")

    periods = database.get_periods()

    if len(periods) == 0:
        st.info("No period records yet. Add your first record above.")
    else:
        for period in periods:
            period_id, start, end = period

            with st.container(border=True):
                st.write(f"**Start:** {start}")
                st.write(f"**End:** {end}")

                if st.button("Delete record", key=f"delete_{period_id}"):
                    database.delete_period(period_id)
                    st.success("Record deleted.")
                    st.rerun()


elif page == "Daily Journal":
    st.title("📔 Your Daily Journal")
    st.write("A little space to check in with yourself.")

    log_date = st.date_input("Choose a date", value=date.today())

    st.write("### How are you feeling?")

    mood_options = [
        "Happy", "Calm", "Anxious", "Sad",
        "Irritated", "Tired", "Okay"
    ]

    with st.form("journal_form"):
        mood = st.selectbox("Mood", mood_options)

        energy = st.slider(
            "Energy level",
            min_value=1,
            max_value=5,
            value=3,
            help="1 = Very low energy, 5 = Very high energy"
        )

        symptoms = st.multiselect(
            "Symptoms (select all that apply)",
            [
                "Cramps", "Headache", "Bloating", "Fatigue",
                "Back pain", "Acne", "Breast tenderness",
                "Nausea", "None"
            ]
        )

        notes = st.text_area(
            "Personal notes (optional)",
            placeholder="Anything you'd like to remember..."
        )

        submitted = st.form_submit_button("Save my entry")

        if submitted:
            if log_date > date.today():
                st.error("You cannot record a future date.")
            elif "None" in symptoms and len(symptoms) > 1:
                st.error("Choose None by itself or select actual symptoms.")
            else:
                database.save_daily_log(
                    log_date.isoformat(),
                    mood,
                    energy,
                    ", ".join(symptoms),
                    notes
                )
                st.success("Your journal entry has been saved! 💜")
                st.rerun()

    st.divider()
    st.subheader("Your past entries")

    logs = database.get_daily_logs()

    if len(logs) == 0:
        st.info("No journal entries yet. Your first check-in can start here.")
    else:
        for log in logs:
            log_id, log_day, log_mood, log_energy, log_symptoms, log_notes = log

            with st.expander(f"{log_day} — {log_mood}"):
                st.write(f"**Energy:** {log_energy}/5")
                st.write(f"**Symptoms:** {log_symptoms or 'None recorded'}")

                if log_notes:
                    st.write(f"**Notes:** {log_notes}")

                if st.button("Delete entry", key=f"log_{log_id}"):
                    database.delete_daily_log(log_id)
                    st.success("Entry deleted.")
                    st.rerun()


elif page == "Insights":
    st.title("✨ Your Insights")
    st.write("Explore patterns in your cycle and daily wellbeing.")

    st.subheader("🌸 Cycle Statistics")

    df = analytics.get_cycle_data()

    if df.empty:
        st.info("Add period records to start exploring your cycle.")
    else:
        valid_cycles = df["Cycle Length"].dropna()

        col1, col2, col3 = st.columns(3)

        with col1:
            if len(valid_cycles) > 0:
                st.metric(
                    "Average Cycle",
                    f"{valid_cycles.mean():.1f} days"
                )
            else:
                st.metric("Average Cycle", "Not available")

        with col2:
            st.metric(
                "Average Period",
                f"{df['Period Length'].mean():.1f} days"
            )

        with col3:
            st.metric("Periods Recorded", len(df))

        fig = analytics.plot_cycle_lengths()

        if fig is not None:
            st.pyplot(fig)
            import matplotlib.pyplot as plt
            plt.close(fig)

    st.divider()
    st.subheader("☁️ Mood and Energy")

    mood_df = analytics.get_mood_data()

    if mood_df.empty:
        st.info("Add journal entries to see your mood and energy insights.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            fig = analytics.plot_mood_counts()
            if fig is not None:
                st.pyplot(fig)
                import matplotlib.pyplot as plt
                plt.close(fig)

        with col2:
            fig = analytics.plot_energy()
            if fig is not None:
                st.pyplot(fig)
                import matplotlib.pyplot as plt
                plt.close(fig)

        st.caption(
            "These charts describe your recorded entries; "
            "they do not establish medical causes or diagnoses."
        )


elif page == "Settings":
    st.title("⚙️ Settings")
    st.write("Manage your personal data and privacy.")

    st.subheader("📥 Export your data")

    periods, logs = database.export_all_data()

    period_df = pd.DataFrame(
        periods,
        columns=["Start Date", "End Date"]
    )

    log_df = pd.DataFrame(
        logs,
        columns=["Date", "Mood", "Energy", "Symptoms", "Notes"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "Download Period History",
            data=period_df.to_csv(index=False),
            file_name="luna_periods.csv",
            mime="text/csv"
        )

    with col2:
        st.download_button(
            "Download Daily Journal",
            data=log_df.to_csv(index=False),
            file_name="luna_journal.csv",
            mime="text/csv"
        )

    st.caption(
        "CSV files can be opened in spreadsheet applications. "
        "Keep downloaded files private."
    )

    st.divider()
    st.subheader("🗑️ Delete your data")

    period_count, daily_count = database.get_data_counts()

    st.write(f"Period records: **{period_count}**")
    st.write(f"Journal entries: **{daily_count}**")

    st.warning(
        "Deleting all records is permanent. "
        "Export your data first if you want a backup."
    )

    confirm = st.checkbox(
        "I understand that this will permanently delete all my records."
    )

    if st.button("Delete all my data", type="primary"):
        if confirm:
            database.delete_all_data()
            st.success("All period and journal records have been deleted.")
            st.rerun()
        else:
            st.error("Please confirm before deleting your data.")

    st.divider()
    st.subheader("🔒 About your privacy")

    st.write(
        "Luna stores its records in a local SQLite database named "
        "`luna.db` in the project directory. The app does not need "
        "an online account for these features. Protect your computer "
        "and any exported CSV files to keep your records private."
    )

    st.caption(
        "Deleting records in the app does not erase previously exported "
        "CSV files or backups."
    )
