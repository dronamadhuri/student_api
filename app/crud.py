from app.database import (
    load_students,
    save_students
)

from app.utils.validators import email_exists


def get_students():
    return load_students()


def get_student(student_id):

    students = load_students()

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def create_student(student):

    students = load_students()

    if email_exists(
        students,
        student["email"]
    ):
        return None

    students.append(student)

    save_students(students)

    return student


def update_student(student_id, updated_student):

    students = load_students()

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students[index] = updated_student

            save_students(students)

            return updated_student

    return None


def delete_student(student_id):

    students = load_students()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            return True

    return False