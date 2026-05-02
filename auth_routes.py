from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def authentication():
    """
    This is the default authentication route from our system. All orders routes require authentication.
    """
    return {"message": "You accessd the default authentication route", "authenticated": False}