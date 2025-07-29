from fastapi import APIRouter, Query
from pydantic import BaseModel

class Video(BaseModel):
    id: int
    title: str
    description: str
    genre: str
    release_year: int
    thumbnail: str
    duration: int

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/', response_model=list[Video], summary="Browse or search videos")
async def list_videos(
    q: str = Query("", description="Search query"),
    genre: str = Query(None, description="Filter by genre"),
    skip: int = 0,
    limit: int = 20
):
    """Browse/search videos catalog."""
    # TODO: Fetch real videos from DB based on search query and genre
    sample = [
        Video(id=1, title="Sample Movie", description="A great movie", genre="Drama", release_year=2022, thumbnail="sample.png", duration=120)
    ]
    return sample

# PUBLIC_INTERFACE
@router.get('/{video_id}', response_model=Video, summary="Get video details")
async def get_video(video_id: int):
    """Get metadata/details for a specific video."""
    # TODO: Fetch video metadata from DB
    return Video(id=video_id, title="Sample Movie", description="Some info", genre="Action", release_year=2023, thumbnail="movie.png", duration=110)
