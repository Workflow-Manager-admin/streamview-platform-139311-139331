from fastapi import APIRouter
from pydantic import BaseModel, Field

class ProfileBase(BaseModel):
    name: str = Field(..., description="Name for the profile")
    avatar: str = Field(..., description="URL for avatar image")

class ProfileResponse(ProfileBase):
    id: int

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/', response_model=list[ProfileResponse], summary="List user profiles")
async def list_profiles():
    """List all profiles for the authenticated user."""
    # TODO: Fetch from DB
    return [ProfileResponse(id=1, name="Kid", avatar="avatar1.png")]

# PUBLIC_INTERFACE
@router.post('/', response_model=ProfileResponse, summary="Create new profile")
async def create_profile(profile: ProfileBase):
    """Create a new user profile."""
    # TODO: Insert into DB
    return ProfileResponse(id=2, name=profile.name, avatar=profile.avatar)
