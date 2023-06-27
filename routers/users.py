from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client

router = APIRouter(prefix='/users', 
                   tags = ['users'], 
                   responses={status.HTTP_404_NOT_FOUND: {'message':'No encontrado'}})


usersList = []

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
    
@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    # if(type(searchUser(user.id)) == User):
    #     raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail= 'El usuario ya existe')
    # else:
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id":id}))

    return User(**new_user)

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