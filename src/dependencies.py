from typing import Annotated
from secrets import compare_digest

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasicCredentials

from src.core.db import get_user
from src.core.security import basic_auth, pwd_context
from src.core.settings import settings
from src.schemas import UserBase


unauthrized_ex = HTTPException(
    status.HTTP_401_UNAUTHORIZED, 
    detail='Incorrect username or password',
    headers={'WWW-Authenticate': 'Basic'}
)
auth = Annotated[HTTPBasicCredentials, Depends(basic_auth)]


def auth_user(creds: auth) -> UserBase:
    user = get_user(creds.username)
    if user and pwd_context.verify(creds.password, user.hashed_password):
        return UserBase.model_validate(user)

    pwd_context.dummy_verify()
    raise unauthrized_ex


def auth_dev(creds: auth) -> None:
    if (
        compare_digest(creds.username, settings.docs_user) and
        compare_digest(creds.password, settings.docs_password)
    ):
        return None 
    raise unauthrized_ex 
