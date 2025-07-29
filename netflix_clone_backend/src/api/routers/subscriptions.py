from fastapi import APIRouter
from pydantic import BaseModel

class SubscriptionStatus(BaseModel):
    is_active: bool
    plan_name: str
    expires_at: str

router = APIRouter()

# PUBLIC_INTERFACE
@router.get('/status', response_model=SubscriptionStatus, summary="Get subscription status")
async def get_subscription_status():
    """Returns user subscription and plan status."""
    # TODO: Fetch real subscription status from DB/payment platform
    return SubscriptionStatus(is_active=True, plan_name="Premium", expires_at="2099-01-01T00:00:00Z")
