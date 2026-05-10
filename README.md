# Personal Notes Manager

## Project Description

Personal Notes Manager is a simple command-line application written in Python that allows users to create, view, search, and delete personal notes. The notes are stored in a text file (`notes.txt`) so they can be accessed again whenever the program is run.

This project is designed to help beginners practice:

- Python programming
- File handling
- Functions
- Loops and conditionals
- Linux command-line operations
- Using Vim or Nano for editing files



Requirements

1. Python 3.x
2. Linux, macOS, Windows, or Termux on Android



## How to Run the Project

###  Project Setup

1. Create the project directory and navigate into it:


```bash
mkdir -p ~/projects/notes_manager
cd ~/projects/notes_manager


---

## Features

The application provides the following features:

1. **Add Note** – Save a new note to the notes file.
2. **View Notes** – Display all saved notes.
3. **Search Notes** – Find notes containing a specific keyword.
4. **Delete All Notes** – Remove all notes from the file.
5. **Exit** – Close the application.

---


## Commands Used

| Command | Purpose |
|---------|---------|
| `mkdir -p ~/projects/notes_manager` | Create project folder |
| `cd ~/projects/notes_manager` | Enter project folder |
| `touch notes.py notes.txt README.md` | Create files |
| `vim notes.py` | Edit Python code |
| `python notes.py` | Run the application |
| `cat notes.txt` | View saved notes |



## Project Structure


```text
notes_manager/
├── notes.py
├── notes.txt
└── README.md


| File | Purpose |
|------|---------|
| `notes.py` | Main Python application |
| `notes.txt` | Stores notes |
| `README.md` | Documentation
