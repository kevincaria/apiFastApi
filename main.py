from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

# Documentación con Swagger http://127.0.0.1:8000/docs
# Documentación con Redocly http://127.0.0.1:8000/redoc
# uvicorn main:app --reload para arrancar la app y ctrl + c para detenerla

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

# Resources 
#app.mount('/static', StaticFiles(directory='static', name='static') ) #Faltan agregar recursos