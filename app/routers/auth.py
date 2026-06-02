from fastapi import APIRouter
from app.schemas import LoginRequest
from app.utils.security import create_access_token

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(user: LoginRequest):

    if (
        user.username == "admin"
        and user.password == "admin123"
    ):

        token = create_access_token(
            {"sub": user.username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    return {
        "message": "Invalid credentials"
    }