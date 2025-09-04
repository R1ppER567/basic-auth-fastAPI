from secrets import compare_digest

from src.schemas import UserInDB
from src.core.security import pwd_context


users_db = [
    UserInDB(username='user1', hashed_password=pwd_context.hash('password1')),
    UserInDB(username='user2', hashed_password=pwd_context.hash('password2'))
]


def get_user(username: str) -> UserInDB | None:
    for user in users_db:
        if compare_digest(username.encode(), user.username.encode()):
            return user
    return None
