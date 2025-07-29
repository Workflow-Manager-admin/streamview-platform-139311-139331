from fastapi import APIRouter
from pydantic import BaseModel

class Recommendation(BaseModel):
    video_id: int
    title: str
    reason: str

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/', response_model=list[Recommendation], summary="Get personalized recommendations")
async def get_recommendations():
    """Returns personalized video recommendations."""
    # TODO: Implement using collaborative filtering/content-based
    return [
        Recommendation(video_id=2, title="Another Movie", reason="Because you watched Action films")
    ]
