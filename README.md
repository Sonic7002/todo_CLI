# Todo CLI

A simple and lightweight command-line todo manager built in Python.  \
Manage your tasks directly from the terminal with easy commands, inspired by `git`-style CLI tools.\
Project idea from: https://roadmap.sh/projects/task-tracker
---

## Features

- Add, update, and delete tasks
- Mark tasks as **in-progress** or **done**
- List tasks with optional status filtering (`todo`, `done`, `in-progress`)
- Persistent storage using a local JSON file
- Fully CLI-driven, no GUI needed
- Easy to install and use

---

## Installation

**1. Clone the repository:**

```bash
git clone <your-repo-url>
cd todo_cli
```

**2. Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

**3. Install the package in editable mode:**
```bash
pip install -e .
```

**4. Verify installation:**
```bash
todo --help
```

**5. Usage**

### The CLI supports the following commands:
**Add a task**
```bash
todo add "Buy groceries"
```
**Update a task**
```bash
todo update 1 "Buy groceries and lunch"
```
**Delete a task**
```bash
todo delete 1
```
**Mark a task as in-progress**
```bash
todo mark-in-progress 2
```
**Mark a task as complete**
```bash
todo mark-done 1
```
### List tasks

**List all tasks**
```bash
todo list
```
**List only completed tasks**
```bash
todo list done
```
**List only pending tasks**
```bash
todo list todo
```
**List only in-progress tasks**
```bash
todo list in-progress
```
---
# Notes

The task data is stored in a local tasks.json file. This file is ignored in git to prevent committing runtime data.

If tasks.json does not exist, it will be created automatically.

This CLI uses Python 3.11+ and requires no external dependencies other than the standard library.

---
# Contributing

Contributions are welcome! Please:

- Fork the repository

- Create a branch for your feature/fix

- Submit a pull request with a clear description of your changes
---
# Future Scope

### The todo-cli project provides a solid foundation for a terminal-based task manager. Potential future enhancements include:

**Persistent storage improvements:**

- Support for databases like SQLite or PostgreSQL for larger task sets and multi-user support.

**Advanced task features:**

- Due dates, priorities, tags, and recurring tasks.

- Task search and filtering by multiple criteria.

**Enhanced CLI experience:**

- Interactive mode for browsing and updating tasks.

- Color-coded outputs for task status (e.g., red for overdue, green for completed).

**Integration and automation:**

- Sync with cloud services or calendars.

- Notification system for reminders.

**Packaging and distribution:**

- Publish to PyPI for global installation.

- Prebuilt binaries for platforms without Python.
---

# License

This project is licensed under the MIT License.

---
### Developed by: Srijan Kargupta
### Copyright (c) 2025 Srijan Kargupta