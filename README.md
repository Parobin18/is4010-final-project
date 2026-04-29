# PyTask: CLI Task Manager

## What it does
PyTask is a lightweight command-line application built in Python that helps you track your daily to-dos. It stores your tasks locally in a JSON file, allowing you to add tasks, view them, and check them off as completed without ever leaving your terminal.

## Installation
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/is4010-final-project.git`
2. Navigate to the directory: `cd is4010-final-project`
3. (Optional) Create a virtual environment and install test dependencies: `pip install pytest`

## Usage
Run the application using Python. You can use the `add`, `list`, or `done` commands.

## Examples
* **Add a task:** `python task_manager.py add "Finish IS4010 Project"`
* **View all tasks:** `python task_manager.py list`
  *(Output: 1. [ ] Finish IS4010 Project)*
* **Mark task as complete:** `python task_manager.py done 1`
  *(Output: Marked task #1 as complete.)*

## Known Limitations / Future Ideas
* Currently, you cannot delete a task entirely, only mark it as done.
* Future versions could include a `clear` command to remove completed tasks to keep the JSON file tidy. # IS4010Final
Final Project for IS4010
