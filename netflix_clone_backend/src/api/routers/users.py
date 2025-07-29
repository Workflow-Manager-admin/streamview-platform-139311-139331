from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/me', response_model=UserResponse, summary="Get current user")
async def get_current_user():
    """Get details of the currently authenticated user."""
    # TODO: Fetch user from DB/session
    return UserResponse(id=1, email="user@email.com", full_name="John Doe", is_active=True)
