from fastapi import FastAPI

from app.routers.students import router as student_router
from app.routers.auth import router as auth_router

from app.middleware.request_logger import (
    RequestLoggerMiddleware
)

app = FastAPI(
    title="Student Management API",
    version="2.0",
    description="CRUD API using FastAPI"
)

app.add_middleware(
    RequestLoggerMiddleware
)

app.include_router(student_router)
app.include_router(auth_router)


@app.get("/")
def home():

    return {
        "message":
        "Student API Running"
    }