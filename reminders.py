
import streamlit as st
import cycle


def show_reminder():
    message = cycle.get_prediction_message()

    st.subheader("🔔 Period Reminder")
    st.info(message)

    st.caption(
        "This is an estimate based on recorded cycle dates, "
        "not a medical prediction or an external notification."
    )
