"""COMP 3005 Assignment 3 - Question 1

Command-line application that connects to a PostgreSQL database and performs
CRUD operations on the students table.
"""

from datetime import datetime
import psycopg2

# TODO: connection settings (host, port, database, user, password)


def get_all_students():
    """Retrieve and display every row of the students table."""
    with psycopg2.connect() as connection:
        students = connection.execute(
            """
            SELECT student_id, first_name, last_name, email, enrollment_date
            FROM student
            ORDER BY student_id
            """
        ).fetchall()

    if not students:
        print("No students found.")
        return

    print("ID | First name | Last name | Email | Enrollment date")
    for student_id, first_name, last_name, email, enrollment_date in students:
        print(f"{student_id} | {first_name} | {last_name} | {email} | {enrollment_date}")


def add_student(first_name, last_name, email, enrollment_date):
    """Insert a new student record."""
    with psycopg2.connect() as connection:
        (student_id,) = connection.execute(
            """
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUE (%s, %s, %s, %s)
            RETURNING student_id
            """,
            (first_name, last_name, email, enrollment_date)
        ).fetchall()
        return student_id


def update_student_email(student_id, new_email):
    """Update the email address of the student with the given id."""
    # TODO
    pass


def delete_student(student_id):
    """Delete the student record with the given id."""
    # TODO
    pass


def main():
    """Menu loop so each function can be demonstrated in the video."""
    # TODO
    pass


if __name__ == "__main__":
    main()
