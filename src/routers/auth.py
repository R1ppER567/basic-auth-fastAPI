from typing import Annotated

from fastapi import APIRouter, Depends

from src.core.db import users_db
from src.core.security import pwd_context
from src.schemas import UserBase, User, UserInDB
from src.dependencies import auth_user


router = APIRouter(tags=['auth']) 


@router.post('/register')
async def register(user: User) -> dict[str, str]:
    users_db.append(UserInDB(
        username=user.username, 
        hashed_password=pwd_context.hash(user.password)     
    ))
    return {'message': f'{user.username} was successfully registrated'}


@router.get('/login')
async def login(user: Annotated[UserBase, Depends(auth_user)]) -> dict[str, str]:
    return {'message': f'Welcome, {user.username}'}
