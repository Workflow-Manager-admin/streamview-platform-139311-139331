from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field

# Models
class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., description="User password")

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: str = Field(..., description="Name of the user")

class RegisterResponse(BaseModel):
    user_id: int
    email: EmailStr

router = APIRouter()

# Routes

# PUBLIC_INTERFACE
@router.post('/login', response_model=LoginResponse, summary="User Login", tags=["Auth"])
async def login(request: LoginRequest):
    """Authenticate the user and return access token."""
    # TODO: Implement authentication logic
    return LoginResponse(access_token="dummy-token", token_type="bearer")

# PUBLIC_INTERFACE
@router.post('/register', response_model=RegisterResponse, summary="User Registration", tags=["Auth"])
async def register(request: RegisterRequest):
    """Register a new user and return user details."""
    # TODO: Implement registration logic
    return RegisterResponse(user_id=1, email=request.email)

# PUBLIC_INTERFACE
@router.post('/refresh-token', response_model=LoginResponse, summary="Refresh Access Token", tags=["Auth"])
async def refresh_token():
    """Refresh and return a new access token."""
    # TODO: Implement refresh logic
    return LoginResponse(access_token="dummy-refresh-token", token_type="bearer")
