from fastapi import APIRouter, Depends
from models import User
from dependencies import catch_session
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def authentication():
    """
    This is the default authentication route from our system. All orders routes require authentication.
    """
    return {"message": "You accessd the default authentication route", "authenticated": False}

@auth_router.post("/creatAccount")
async def createAccount(email: str, password: str, name: str, session = Depends(catch_session)):
    user = session.query(User).filter(User.email==email).first()
    if user:
        return{"Message": "User already registered with this email"}
    else:
        cryptedPassword = bcrypt_context.hash(password)
        newUser = User(name, email, cryptedPassword)
        session.add(newUser)
        session.commit()
        return {"Message": "New User sucessfully registered"}