
import pandas as pd
import matplotlib.pyplot as plt
import database
import cycle


def get_cycle_data():
    periods = database.get_periods()

    if len(periods) == 0:
        return pd.DataFrame()

    data = []

    for period in periods:
        data.append({
            "Start Date": pd.to_datetime(period[1]),
            "End Date": pd.to_datetime(period[2])
        })

    df = pd.DataFrame(data)
    df = df.sort_values("Start Date")

    df["Cycle Length"] = df["Start Date"].diff().dt.days
    df["Period Length"] = (
        df["End Date"] - df["Start Date"]
    ).dt.days + 1

    return df


def get_mood_data():
    logs = database.get_daily_logs()

    if len(logs) == 0:
        return pd.DataFrame()

    data = []

    for log in logs:
        data.append({
            "Date": pd.to_datetime(log[1]),
            "Mood": log[2],
            "Energy": log[3],
            "Symptoms": log[4] or ""
        })

    return pd.DataFrame(data)


def plot_cycle_lengths():
    df = get_cycle_data()
    df = df.dropna(subset=["Cycle Length"])

    if df.empty:
        return None

    fig, ax = plt.subplots()
    ax.plot(
        df["Start Date"],
        df["Cycle Length"],
        marker="o"
    )
    ax.set_title("Cycle Length Over Time")
    ax.set_xlabel("Period Start Date")
    ax.set_ylabel("Cycle Length (days)")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()

    return fig


def plot_mood_counts():
    df = get_mood_data()

    if df.empty:
        return None

    counts = df["Mood"].value_counts()

    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_title("Mood Check-ins")
    ax.set_xlabel("Mood")
    ax.set_ylabel("Number of Days")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()

    return fig


def plot_energy():
    df = get_mood_data()

    if df.empty:
        return None

    df = df.sort_values("Date")

    fig, ax = plt.subplots()
    ax.plot(
        df["Date"],
        df["Energy"],
        marker="o"
    )
    ax.set_title("Daily Energy Levels")
    ax.set_xlabel("Date")
    ax.set_ylabel("Energy (1–5)")
    ax.set_ylim(0, 5)
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()

    return fig
