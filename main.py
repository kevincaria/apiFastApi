from fastapi import FastAPI
from routers import users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

# Documentación con Swagger http://127.0.0.1:8000/docs
# Documentación con Redocly http://127.0.0.1:8000/redoc
# uvicorn main:app --reload para arrancar la app y ctrl + c para detenerla

app = FastAPI()

# Routers
app.include_router(users.router)
app.include_router(jwt_auth_users.router)

# Resources 
#app.mount('/static', StaticFiles(directory='static', name='static') ) #Faltan agregar recursos