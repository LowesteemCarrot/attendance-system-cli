# Attendance CLI

A simple command-line face-recognition attendance system built with Python, OpenCV, and MySQL/MariaDB.

This tool allows you to:
- Register students with facial encodings
- Scan faces via webcam to mark attendance
- Export attendance logs to CSV

---

## Available Commands

### 1. Register a student
Register a new student and capture their face using the webcam.

**Usage:**
```bash
attendance register "<student_name>" <student_id>
```

**Example:**
```bash
attendance register "Rahul Kumar" 12
```

**What it does:**
- Opens webcam  
- Detects face  
- Captures encoding  
- Saves to database  
- Press `Q` to capture and save

---

### 2. Scan attendance
Start face-recognition mode and mark students present.

**Usage:**
```bash
attendance scan
```

**What it does:**
- Opens webcam  
- Reads all saved face encodings  
- Marks a student "present" when recognized  
- Skips duplicates  
- Press `Q` to exit

---

### 3. Export attendance
Export all attendance records to a CSV file.

**Usage:**
```bash
attendance export
```

**Result:**
Creates a file:
```
attendance_export.csv
```
containing:
- Student ID
- Student name
- Date
- Time
- Status

---

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

Install the CLI tool (editable mode):
```bash
pip install -e .
```

This enables the command:
```
attendance
```

---

## Requirements

- Python 3.10+
- OpenCV
- face_recognition
- mysql-connector-python
- Webcam
- MySQL or MariaDB running and configured

---

## Database Notes

The database must contain a `students` table with a `face_encoding` column of type `LONGBLOB`.

Example:
```sql
ALTER TABLE students ADD face_encoding LONGBLOB;
```

---

## Notes

- Press `Q` during webcam actions to confirm or stop.
- Ensure the database connection settings are correct in `config/config.json`.

