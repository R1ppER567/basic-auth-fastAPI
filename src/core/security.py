from fastapi.security import HTTPBasic
from passlib.context import CryptContext


basic_auth = HTTPBasic()
pwd_context = CryptContext(schemes=['bcrypt'])
