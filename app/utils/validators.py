def email_exists(students, email):

    for student in students:
        if student["email"] == email:
            return True

    return False