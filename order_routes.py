from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def order():
    """
    This is the default orders route from our system.
    """
    return {"message": "You accessd the order route"}