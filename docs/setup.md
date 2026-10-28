
# Setup Instructions — Smart Campus 360

## Requirements

- Python 3.11 or newer
- GitHub repository cloned or downloaded to your computer
- Internet connection to install Python packages

## Installation on Windows

1. Open the project folder in File Explorer.
2. Click the address bar, type `cmd`, and press Enter.
3. Create a virtual environment:

   `py -m venv .venv`

4. Activate it:

   `.venv\Scripts\activate`

5. Install the packages:

   `python -m pip install -r requirements.txt`

6. Start the application:

   `python -m uvicorn backend.app:app --reload`

7. Open the dashboard:

   `http://127.0.0.1:8000`

8. Open the API documentation:

   `http://127.0.0.1:8000/docs`

## Verify the API

Open `http://127.0.0.1:8000/api/health`.

A successful response should identify the project and report a status of `ok`.

## Test the Complaint Workflow

1. Open the dashboard.
2. Enter a sample issue category, location, and description.
3. Click Submit complaint.
4. Confirm that the new complaint appears in the complaint tracker.
5. Use Mark resolved to update its status.

## Database

The application creates `smartcampus.db` locally when the backend starts. It stores demonstration complaint records. This local database file is excluded from Git by `.gitignore`.

## Troubleshooting

- If `py` is not recognised, install Python and reopen Command Prompt.
- If a port is already in use, stop the other server or configure another port.
- If the dashboard cannot load, confirm the backend is running and visit `/api/health`.
- If package installation fails, check the Python version and internet connection.

## Shutdown

Press `Ctrl + C` in the terminal running the server.
