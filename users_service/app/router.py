from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from app.auth import auth_backend
from app.manager import get_user_manager
from app.models import User
from app.schemas import UserRead, UserCreate

router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@router.get("/unprotected-route")
def unprotected_route():
    return "Hello, anonym"
