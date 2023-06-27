from fastapi import APIRouter, HTTPException
from pydantic import BaseModel



router = APIRouter(prefix='/users', 
                   tags = ['users'], 
                   responses={404: {'message':'No encontrado'}})

# Entidad Users
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

usersList = [User(id= 1,  name='Kevin', surname='Caria', url='https=//kevin.com', age=29),
            User(id= 2,  name='Gaspar', surname='Caria', url='https=//gaspar.com', age=70),
            User(id= 3,  name='Hidalgo', surname='Caria', url='https=//hidalgo.com', age=85)]

@router.get('/',  status_code=200)
async def users():
    return usersList

#Por path http://127.0.0.1:8000/userpath/1
@router.get('/{id}',  status_code=200)
async def user(id:int):
    return searchUser(id)
    
# Por query http://127.0.0.1:8000/userquery?id=2
# @router.get('/',  status_code=200)
# async def user(id:int):
#     return searchUser(id)
    
@router.post('/', response_model=User, status_code=201)
async def user(user: User):
    response = ' '
    if(type(searchUser(user.id)) == User):
        raise HTTPException(status_code=204, detail= 'El usuario ya existe')
    else:
        usersList.routerend(user)


@router.put('/', status_code=200)
async def user(user: User):

    found = False
    response = ' '

    #Solo por probar otra forma de buscar el usuario, podria seguir usando searchUser
    for index, savedUser in enumerate(usersList):
        if savedUser.id == user.id:
            usersList[index] = user
            found = True
        
    if found is False:
        raise HTTPException(status_code=404, detail= 'No se ha encontrado el usuario')
    

@router.delete('/{id}', status_code=200)
async def user(id:int):
    found = False
    response = ' '

    #Solo por probar otra forma de buscar el usuario, podria seguir usando searchUser
    for index, savedUser in enumerate(usersList):
        if savedUser.id == user.id:
            del usersList[index] 
            found = True
        
    if found is False:
        raise HTTPException(status_code=400, detail=  'No se ha eliminado el usuario')
    
    return response

def searchUser(id: int):
    users = filter(lambda user: user.id == id, usersList)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=400, detail= 'El usuario ya existe')