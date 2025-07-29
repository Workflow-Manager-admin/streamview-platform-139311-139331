from fastapi import APIRouter
from pydantic import BaseModel

class HistoryItem(BaseModel):
    video_id: int
    watched_at: str
    progress_seconds: int

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/', response_model=list[HistoryItem], summary="Get watch history")
async def get_watch_history():
    """Returns user's watch history."""
    # TODO: Fetch history from DB
    return [HistoryItem(video_id=1, watched_at="2024-06-18T10:01:00Z", progress_seconds=600)]
