from fastapi import APIRouter
from pydantic import BaseModel

class PaymentStartRequest(BaseModel):
    plan_id: int

class PaymentStatusResponse(BaseModel):
    status: str
    message: str

router = APIRouter()

# PUBLIC_INTERFACE
@router.post('/start', response_model=PaymentStatusResponse, summary="Start payment")
async def start_payment(request: PaymentStartRequest):
    """Begin payment for subscription plan."""
    # TODO: Integrate payment processor here
    return PaymentStatusResponse(status="success", message="Dummy: Payment started")

# PUBLIC_INTERFACE
@router.get('/history', response_model=list[PaymentStatusResponse], summary="Get user payment history")
async def get_payment_history():
    """Retrieve list of payment records for current user."""
    # TODO: Query payments from DB
    return [PaymentStatusResponse(status="success", message="Paid on 2023-01-31")]
