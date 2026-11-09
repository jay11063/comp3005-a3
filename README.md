# COMP 3005 Assignment 3 — Student Records Application

A command-line application that connects to a PostgreSQL database and performs
CRUD operations on a `students` table.

Jaeyoon Lee — 101272513 — COMP3005 B, Fall 2026

## Demonstration video

<!-- TODO: paste the video link here before submitting -->

## Requirements

<!-- TODO: PostgreSQL version, Python version, and the driver you used -->

## Setup

1. Create the database

<!-- TODO: the exact steps, e.g. createdb comp3005_a3, or the pgAdmin equivalent -->

2. Create the table and load the initial data

<!-- TODO: how to run sql/schema.sql -->

3. Install dependencies

<!-- TODO: pip install ... -->

4. Configure the connection

<!-- TODO: say where the host, port, database, user and password are set -->

## Running the application

<!-- TODO: the command that starts the app, and what the user sees -->

## Functions

| Function | Description |
| --- | --- |
| `getAllStudents()` | Retrieves and displays every row of the `students` table. |
| `addStudent(first_name, last_name, email, enrollment_date)` | Inserts a new student record. |
| `updateStudentEmail(student_id, new_email)` | Updates the email address of the student with the given id. |
| `deleteStudent(student_id)` | Deletes the student record with the given id. |

## Repository layout

```
sql/schema.sql   Table definition and the initial data
src/app.py       Application code
```
