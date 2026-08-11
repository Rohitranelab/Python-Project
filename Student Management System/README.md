# Student Management System

A simple command-line Student Management System built in Python. It lets you add, view, update, and delete student records, along with their subjects and marks. All data is persisted locally in a JSON file (`students.json`).

## Features

- **Add Student Information** — Store name, mobile number, date of birth, standard, and division.
- **Display Student Information** — Look up and view a specific student's details.
- **Add Subject and Marks** — Record multiple subjects and marks for a student.
- **Display Marks** — View all subjects and marks for a specific student.
- **Display All Students** — View complete records for every student in the system.
- **Delete Student** — Remove a student's record permanently.
- **Persistent Storage** — All data is automatically saved to and loaded from `students.json`.

## Requirements

- Python 3.x
- No external libraries required (uses only Python's built-in `json` and `os` modules)

## How to Run

1. Make sure Python 3 is installed on your system.
2. Save the script as `student_management_system.py`.
3. Open a terminal in the same directory and run:

   ```bash
   python student_management_system.py
   ```

4. Follow the on-screen menu to manage student records.

## Menu Options

```
1. Add Student Information
2. Display Student Information
3. Add Subject and Marks
4. Display Marks
5. Display All Students
6. Delete Student
7. Exit
```

## Data Storage

Student records are stored in a file named `students.json`, created automatically in the same directory as the script the first time you add a student. Example structure:

```json
{
    "Rohit Rane": {
        "mobile": "7894561230",
        "dob": "25/05/2005",
        "standard": "3rd Year",
        "division": "A",
        "subjects": {
            "Python": 74,
            "Machine Learning": 45
        }
    }
}
```

## Project Structure

```
Student Management System/
│
├── student_management_system.py   # Main application script
├── students.json                  # Auto-generated data file (created on first run)
└── README.md                      # Project documentation
```

## Notes / Possible Improvements

- No input validation currently exists for mobile numbers, marks (e.g., negative values), or duplicate subjects.
- Marks are stored as raw integers with no cap (e.g., no check for max marks like 100).
- Student lookup is name-based, so two students with the same name will conflict (the second entry will be blocked as "already exists").
