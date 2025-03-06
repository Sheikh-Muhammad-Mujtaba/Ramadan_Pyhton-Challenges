# Todo App CLI 

This is a simple **Command Line Interface (CLI)** Todo App built using Python and the `click` library. It allows you to manage your tasks by adding, listing, marking as complete, and removing tasks. Tasks are stored in a JSON file (`todo.json`) for persistence.

---

## Features

- **Add a Task**: Add a new task to your todo list.
- **List Tasks**: View all tasks with their status (done or not done).
- **Mark as Complete**: Mark a specific task as done.
- **Remove a Task**: Delete a task from the list.

---

## Prerequisites

1. **Python 3.7+**: Ensure Python is installed on your system.
2. **Click Library**: Install the `click` library to run the CLI:
   ```bash
   pip install click
   ```

---

## How to Use

### 1. **Clone or Download the Script**
   - Save the script as `todo_cli.py`.

### 2. **Run the CLI**
   - Open a terminal and navigate to the directory where the script is saved.
   - Run the script using Python:
     ```bash
     python todo_cli.py
     ```

---

## Available Commands

### 1. **Add a Task**
   - Add a new task to the todo list.
   - **Command**:
     ```bash
     python todo_cli.py add "Your Task Here"
     ```
   - **Example**:
     ```bash
     python todo_cli.py add "Buy groceries"
     ```
   - **Output**:
     ```
     Task added successfully: Buy groceries
     ```

---

### 2. **List All Tasks**
   - View all tasks with their status (done or not done).
   - **Command**:
     ```bash
     python todo_cli.py list
     ```
   - **Example Output**:
     ```
     1. Buy groceries - [Not done ❌]
     2. Finish report - [Done ✅]
     ```

---

### 3. **Mark a Task as Complete**
   - Mark a specific task as done by providing its task number.
   - **Command**:
     ```bash
     python todo_cli.py complete <task_number>
     ```
   - **Example**:
     ```bash
     python todo_cli.py complete 1
     ```
   - **Output**:
     ```
     Task 1 marked as done
     ```

---

### 4. **Remove a Task**
   - Remove a task from the list by providing its task number.
   - **Command**:
     ```bash
     python todo_cli.py remove <task_number>
     ```
   - **Example**:
     ```bash
     python todo_cli.py remove 1
     ```
   - **Output**:
     ```
     Task 1 removed successfully
     ```

---

## File Storage

- Tasks are stored in a JSON file named `todo.json` in the same directory as the script.
- The file is automatically created when you add your first task.
- Example `todo.json` content:
  ```json
  [
    {"task": "Buy groceries", "done": false},
    {"task": "Finish report", "done": true}
  ]
  ```

---

## Error Handling

- **Invalid Task Number**: If you provide an invalid task number (e.g., a number that doesn't exist in the list), the app will display an error message:
  ```
  Invalid task number provided <task_number>
  ```

---

## Customization

- **Colors**: The app uses ANSI escape codes to display colored output. You can customize the colors in the `Colors` class within the script.

---

## Example Workflow

1. Add a task:
   ```bash
   python todo_cli.py add "Buy groceries"
   ```
2. List tasks:
   ```bash
   python todo_cli.py list
   ```
3. Mark a task as complete:
   ```bash
   python todo_cli.py complete 1
   ```
4. Remove a task:
   ```bash
   python todo_cli.py remove 1
   ```

