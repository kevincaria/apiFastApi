from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl='login')

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
        'username': 'kcaria',
        'full_name': 'Kevin Caria',
        'email': 'kevincaria@gmail.com',
        'diabled': True,
        'password': '123456'
    },
    'kevincaria2': {
        'username': 'kcaria2',
        'full_name': 'Kevin Caria2',
        'email': 'kevincaria2@gmail.com',
        'diabled': True,
        'password': '654321'
    }
}

def search_user(username:str):
    if username in users_db:
        return UserDB(users_db[username])
    
@app.post('/login')
async def login(form:OAuth2PasswordRequestForm = Depends()):

    if not users_db.get(form.username):
        raise HTTPException(status_code=400, detail='El usuario no es correcto')
    
    user = search_user(form.username)

    if not form.password == user.password:
        raise HTTPException(status_code=400, detail='La contraseña no es correcta')
    
    return {'access_token': user.username, 'token_type': 'bearer'}

@app.get('/user/me')
async def me(user: User = Depends()):
    return user


