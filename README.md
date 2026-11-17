# Task Manager

## Summary
This app is a miniature command-line task manager. You can add, view, edit, complete, and delete tasks. To ensure persistence, the app creates or maintains a json file with your tasks and metadata. The app starts by first creating or reading the json file. Then, the app prompts the user to utilize the task manager. Once the user exits, the app writes the user's edits to the json file.

## API Import Feature
I added a new feature to task manager. It can now retrieve tasks from a public API and import them into the local JSON database. When you select option 6, instead of exiting (which is now option 7), task manager retrieves the first five incomplete tasks from JSONPlaceholder's /todos endpoint. Then, it reformats and saves those tasks to the existing local json file.

## Requirements
- Python 3.12+

## Running Instructions
1. Make a local copy of this repository.
2. Move into the repository's directory (ex. cd Task_Manager/)
3. Create a virtual environment (if not done already): `python3 -m venv venv`
4. Activate the virtual environment:
    - Linux/macOS: `source venv/bin/activate`
    - Windows Powershell: `.\venv\Scripts\Activate.ps1`
5. Download the required libraries (if not done already): `pip install -r requirements.txt`
6. Enter in your terminal `python3 main.py`
