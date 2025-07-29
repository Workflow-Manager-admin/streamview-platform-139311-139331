from fastapi import APIRouter
from pydantic import BaseModel

class ParentalSettings(BaseModel):
    enabled: bool
    allowed_ratings: list[str]

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/', response_model=ParentalSettings, summary="Get parental control settings")
async def get_settings():
    """Retrieve parental control settings for current user/profile."""
    # TODO: Fetch parental control settings from DB
    return ParentalSettings(enabled=True, allowed_ratings=["G", "PG", "PG-13"])
