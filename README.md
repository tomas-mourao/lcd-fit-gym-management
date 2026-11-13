# LCD Fit – Gym Management System

Console application in Python for managing a gym, **LCD Fit**: members, classes, entry passes and subscriptions.

> **Course:** Programming · BSc in Data Science, ISCTE · Year 1, Semester 1

## Features
- **Members:** create and identify members, buy entry passes, activate or deactivate subscriptions.
- **Classes:** create classes with an instructor and a capacity, enrol and remove members.
- **Admin menu:** add members and classes, search with filters.
- **Member menu:** view and manage your own passes and enrolments.
- **Persistence:** export and import the gym state to and from a text file.

The code is object-oriented, built around the `Membro` (member), `Aula` (class) and `Gym` classes.

## Tech stack
Python 3 (standard library only)

## How to run
```bash
python gym_manager.py
```

To load sample data, import `gym.txt` from the main menu.

> The console interface is in Portuguese.

## Project structure
| File | Description |
|------|-------------|
| `gym_manager.py` | Application source code |
| `gym.txt` | Sample data (members and classes) |
