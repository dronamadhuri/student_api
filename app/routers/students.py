from fastapi import (
    APIRouter,
    HTTPException,
    Query
)

from app.schemas import Student

from app.crud import (
    get_students,
    get_student,
    create_student,
    update_student,
    delete_student
)

from app.utils.pagination import paginate

router = APIRouter(tags=["Students"])


@router.get("/students")
def all_students(
    page: int = Query(1),
    limit: int = Query(5)
):

    students = get_students()

    return {
        "total": len(students),
        "students": paginate(
            students,
            page,
            limit
        )
    }


@router.get("/students/{student_id}")
def single_student(student_id: int):

    student = get_student(student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@router.post("/students")
def add_student(student: Student):

    created = create_student(
        student.model_dump()
    )

    if created is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "Student added",
        "student": created
    }


@router.put("/students/{student_id}")
def edit_student(
    student_id: int,
    student: Student
):

    updated = update_student(
        student_id,
        student.model_dump()
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Updated successfully",
        "student": updated
    }


@router.delete("/students/{student_id}")
def remove_student(student_id: int):

    if not delete_student(student_id):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Deleted successfully"
    }


@router.get("/search")
def search_student(name: str):

    students = get_students()

    result = [
        s
        for s in students
        if name.lower()
        in s["name"].lower()
    ]

    return result