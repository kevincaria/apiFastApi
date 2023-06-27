from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "1660daf98df19700fc322ef1b81587031a7f1bb26851317d7594fb0a2236f2e8"
router = APIRouter(tags = ['login'])

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(BaseModel):
    username:str
    password:str

users_db = {
    'kevincaria': {
        'username': 'kevincaria',
        'full_name': 'Kevin Caria',
        'email': 'kevincaria@gmail.com',
        'disabled': False,
        'password': '$2a$12$Zs5DrJru2RGeNVAS2CSFju/EF2lEbfOgpIwxbD/JWnxyJUE7oESS2'
    },
    'kevincaria2': {
        'username': 'kevincaria2',
        'full_name': 'Kevin Caria2',
        'email': 'kevincaria2@gmail.com',
        'disabled': True,
        'password': '$2a$12$MtN7fY4sJl3D0Cr9f1WpHuKOrXBbuxKNHNomas9Qo4Df6eIPjeD6q'
    }
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Credenciales inválidas', headers={'WWW-Authenticate':'Bearer'})

    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario inactivo')
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_data = users_db.get(form.username)
    if not user_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pass incorrecto")

    access_token = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION),
    }

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user