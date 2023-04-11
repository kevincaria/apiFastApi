from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# Documentación con Swagger http://127.0.0.1:8000/docs
# Documentación con Redocly http://127.0.0.1:8000/redoc
# uvicorn users:app --reload para arrancar la app y ctrl + c para detenerla
app = FastAPI()

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

@app.get('/usersjson')
async def users():
    return [{'name':'Kevin', 'surname':'Caria', 'url':'https://kevin.com', 'age':29},
            {'name':'Gaspar', 'surname':'Caria', 'url':'https://gaspar.com', 'age':70},
            {'name':'Hidalgo', 'surname':'Caria', 'url':'https://hidalgo.com', 'age':85}]

@app.get('/users',  status_code=200)
async def users():
    return usersList

#Por path http://127.0.0.1:8000/userpath/1
@app.get('/user/{id}',  status_code=200)
async def user(id:int):
    return searchUser(id)
    
#Por query http://127.0.0.1:8000/userquery?id=2
@app.get('/userquery',  status_code=200)
async def user(id:int):
    return searchUser(id)
    
@app.post('/user/', response_model=User, status_code=201)
async def user(user: User):
    response = ' '
    if(type(searchUser(user.id)) == User):
        raise HTTPException(status_code=204, detail= 'El usuario ya existe')
    else:
        usersList.append(user)


@app.put('/user/', status_code=200)
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
    

@app.delete('/user/{id}', status_code=200)
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