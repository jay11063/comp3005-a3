"""COMP 3005 Assignment 3 - Question 1

Command-line application that connects to a PostgreSQL database and performs
CRUD operations on the students table.
"""

from datetime import datetime
import psycopg2

import os
from dotenv import load_dotenv

load_dotenv()

DB_SETTINGS = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "student_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
}

def get_all_students():
    """Retrieve and display every row of the students table."""
    try:
        with psycopg2.connect(**DB_SETTINGS) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT student_id, first_name, last_name, email, enrollment_date
                    FROM students
                    ORDER BY student_id;
                    """
                )

                students = cursor.fetchall()

                if not students:
                    print("No students found.")
                    return

                print(f"{'ID':<5} | {'First Name':<15} | {'Last Name':<15} | {'Email':<30} | {'Enrollment Date'}")
                print("-" * 85)
                for student_id, first_name, last_name, email, enrollment_date in students:
                    print(f"{student_id:<5} | {first_name:<15} | {last_name:<15} | {email:<30} | {enrollment_date}")

    except Exception as e:
        print(f"Error: Failed to get all students: {e}")


def add_student(first_name, last_name, email, enrollment_date):
    """Insert a new student record."""
    try:
        with psycopg2.connect(**DB_SETTINGS) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO students (first_name, last_name, email, enrollment_date)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (first_name, last_name, email, enrollment_date)
                )
                connection.commit()
                print(f"Successfully added student [{first_name} {last_name}].")

    except Exception as e:
        print(f"Error: Failed to add student: {e}")


def update_student_email(student_id, new_email):
    """Update the email address of the student with the given id."""
    try:
        with psycopg2.connect(**DB_SETTINGS) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT student_id FROM students WHERE student_id = %s;", 
                    (student_id,)
                )
                if not cursor.fetchone():
                    print(f"Student with the given id {student_id} does not exist.")
                    return
                
                cursor.execute(
                    "UPDATE students SET email = %s WHERE student_id = %s;", 
                    (new_email, student_id)
                )
                connection.commit()
                print(f"Successfully updated email for student ID {student_id} to {new_email}")

    except Exception as e:
        print(f"Error: Failed to update email: {e}")


def delete_student(student_id):
    """Delete the student record with the given id."""
    try:
        with psycopg2.connect(**DB_SETTINGS) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT student_id FROM students WHERE student_id = %s;", 
                    (student_id,),
                )
                if not cursor.fetchone():
                    print(f"Student with the given id {student_id} does not exist.")
                    return
                
                cursor.execute(
                    "DELETE FROM students WHERE student_id = %s;",
                    (student_id,),
                )
                connection.commit()
                print(f"Successfully delete student ID {student_id}")

    except Exception as e:
        print(f"Error: Failed to deleted student: {e}")


def main():
    """Menu loop so each function can be demonstrated in the video."""
    print("COMP3005 Assignment 3 - Student DB")
    while True:
        print("1. List all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            get_all_students()

        elif choice == "2":
            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            email = input("Email: ").strip()
            enrollment_date_string = input("Enrollment date (YYYY-MM-DD): ").strip()
            try:
                enrollment_date = datetime.strptime(enrollment_date_string, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format.")
                continue
            if first_name and last_name and email:
                add_student(first_name, last_name, email, enrollment_date)
            else:
                print("First name, last name, and email are required.")

        elif choice == "3":
            try:
                student_id = int(input("Student ID: "))
                new_email = input("New email: ").strip()
                if new_email:
                    update_student_email(student_id, new_email)
                else:
                    print("Email address cannot be empty.")
            except ValueError:
                print("Student ID must be an integer.")

        elif choice == "4":
            try:
                student_id = int(input("Student ID: "))
                delete_student(student_id)
            except ValueError:
                print("Student ID must be an integer.")

        elif choice == "0":
            return

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
