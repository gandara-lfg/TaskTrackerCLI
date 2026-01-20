# Tasker CLI

A simple command-line task management application built with Python. Track your todos, mark progress, and stay organized—all from your terminal.

## Features

- Add, update, and remove tasks
- Track task status (To do, In Progress, Completed)
- Automatic timestamps for creation and updates
- Persistent storage using JSON
- Simple and intuitive command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tasker-cli.git
cd tasker-cli
```

2. Make sure you have Python 3.10+ installed:
```bash
python --version
```

3. Run the application:
```bash
python3 tasker-cli.py start
```

## Usage

### Getting Started

View all available commands:
```bash
python3 tasker-cli.py help
```

### Commands

#### Add a Task
```bash
python3 tasker-cli.py add "Buy groceries"
```

#### View All Tasks
```bash
python3 tasker-cli.py print
```

#### Update a Task
```bash
python3 tasker-cli.py update <id> "New task description"
```
Example:
```bash
python3 tasker-cli.py update 1 "Buy groceries and cook dinner"
```

#### Remove a Task
```bash
python3 tasker-cli.py remove <id>
```
Example:
```bash
python3 tasker-cli.py remove 1
```

#### Change Task Status
```bash
python3 tasker-cli.py status <id> <status_number>
```

Status options:
- `1` - To do
- `2` - In Progress
- `3` - Completed

Example:
```bash
python3 tasker-cli.py status 1 2
```

## Example Workflow

```bash
# Start the app and see available commands
python3 tasker-cli.py start

# Add some tasks
python3 tasker-cli.py add "Complete homework"
python3 tasker-cli.py add "Study for exam"
python3 tasker-cli.py add "Call mom"

# View all tasks
python3 tasker-cli.py print

# Mark a task as in progress
python3 tasker-cli.py status 1 2

# Update a task description
python3 tasker-cli.py update 2 "Study for Math 313 exam"

# Mark a task as completed
python3 tasker-cli.py status 3 3

# Remove a completed task
python3 tasker-cli.py remove 3
```

## Data Storage

Tasks are stored in `tasks.json` in the same directory as the script. Each task contains:
- `id` - Unique identifier
- `description` - Task description
- `status` - Current status (To do, In Progress, Completed)
- `createdAt` - ISO timestamp of creation
- `updatedAt` - ISO timestamp of last update

Example `tasks.json`:
```json
[
  {
    "id": 1,
    "description": "Complete homework",
    "status": "In Progress",
    "createdAt": "2025-01-19T15:30:00.123456",
    "updatedAt": "2025-01-19T16:45:00.654321"
  }
]
```

## Requirements

- Python 3.10 or higher (uses `match` statement)
- No external dependencies (uses only standard library)

## Project Structure

```
tasker-cli/
├── tasker-cli.py    # Main application file
├── tasks.json       # Task storage (created automatically)
└── README.md        # This file
```

## Future Enhancements

- [ ] Filter tasks by status
- [ ] Add due dates and reminders
- [ ] Sort tasks by priority
- [ ] Export tasks to CSV
- [ ] Add task categories/tags
- [ ] Search functionality

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the MIT License.

## Author

Emilio Gandara

---

Built with ❤️ using Python
