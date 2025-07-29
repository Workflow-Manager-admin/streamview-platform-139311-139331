from fastapi import APIRouter, Path
from pydantic import BaseModel

class VideoPlaybackInfo(BaseModel):
    video_url: str
    drm_token: str | None = None

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/{video_id}', response_model=VideoPlaybackInfo, summary="Get video playback info for streaming")
async def get_stream_info(video_id: int = Path(..., description="ID of the video to play")):
    """Returns the streaming URL and DRM info needed for video playback."""
    # TODO: Generate signed URL, DRM token, etc.
    return VideoPlaybackInfo(video_url=f"https://example.com/video/{video_id}/play.m3u8", drm_token=None)
