# Luna — Menstrual Cycle Tracker and Wellness App

Luna is a Python-based menstrual cycle tracking and wellness application. It helps users record period dates and daily wellness information, review cycle history, view summaries and charts, and export or delete their records.

## Features

- Record and manage period start and end dates.
- Keep a daily journal with mood, energy, symptoms, and notes.
- View cycle and wellness insights through summaries and charts.
- Estimate a possible next period date using previous cycle lengths.
- Store application data in SQLite.
- Export records and manage saved data through the app.
- Use a Streamlit interface with custom styling.

> **Important:** Period predictions are estimates based on recorded dates and may be inaccurate. Luna is a personal tracking tool, not a medical diagnostic system.

## Technology Stack

- **Python** — application logic
- **Streamlit** — user interface
- **SQLite** — database
- **Pandas and NumPy** — data processing and calculations
- **Matplotlib** — charts and visualisations
- **Jupyter Notebook** — demonstration and analysis

## Project Structure

## Project Files

- [Main Streamlit App](app.py)
- [Database Operations](database.py)
- [Cycle Calculations](cycle.py)
- [Analytics](analytics.py)
- [Reminders](reminders.py)
- [Dependencies](requirements.txt)
- [Jupyter Notebook](Luna.ipynb)
- [Project Report](LUNA%20PROJECT%20REPORT.pdf)
- [Streamlit Configuration](.streamlit/config.toml)


## Requirements

- Python 3.10 or later is recommended.
- The Python packages listed in `requirements.txt`.
- VS Code or another Python editor.
- Jupyter support if you want to run the notebook.

## Setup and Run

1. Download or extract the Luna project folder.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Streamlit should open the app in your browser. If it does not, open the local URL shown in the terminal.

SQLite databases are often created automatically when the app initialises its database connection. If the app uses an existing database file, keep it in the location expected by the code.

## Jupyter Notebook

Open `Luna_Project_Notebook_Completed.ipynb` in VS Code or Jupyter and run the cells from top to bottom.

The notebook demonstrates data processing, cycle calculations, visualisations, and SQLite operations. It uses sample data for reproducibility and checks for `luna.db` in the current working directory. The database-inspection section is read-only. The notebook's demonstration database is separate from the app database.

## Data and Privacy

- Treat period and journal records as sensitive personal information.
- Do not include real personal records in public repositories or project submissions.
- The app's database may contain personal information; share it only if necessary and with consent.
- Review the current code before describing any feature as secure, encrypted, or account-protected.

## Limitations

- Cycle estimates are approximate and depend on the quality and amount of recorded data.
- The notebook uses sample records in several analysis sections.
- Features such as email reminders or account-based login should only be considered available if they are implemented and tested in the submitted version.

## Project Deliverables

For the IT Workshop III course submission, prepare:

- The Jupyter Notebook (`.ipynb`).
- The project report in PDF format.
- The Python source files and configuration needed to run and demonstrate the application.
- `requirements.txt` so the required packages can be installed.

Follow your instructor's submission instructions if they specify a particular format or upload method.

## Author

**S. Kamalini**  
B.Tech Computer Science and Engineering  
Indian Institute of Information Technology Kottayam

## Disclaimer

Luna is intended for personal tracking and educational demonstration. It does not provide medical advice or guarantee the accuracy of future period dates.
