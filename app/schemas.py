from pydantic import BaseModel, EmailStr


class Student(BaseModel):
    id: int
    name: str
    department: str
    email: EmailStr


class LoginRequest(BaseModel):
    username: str
    password: str