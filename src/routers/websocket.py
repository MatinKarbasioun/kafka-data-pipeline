from fastapi.routing import APIRoute, APIRouter
from sel
router = APIRouter()


@router.websocket('/ws')
def get_market_stream():
    pass
