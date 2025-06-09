from fastapi import FastAPI
from .db.connection import create_database
from .routers import servicios,clientes

app = FastAPI()
app.include_router(servicios.router)
app.include_router(clientes.router)

#DATABASE
create_database()

@app.get('/')
async def root ():
    return 'Welcome to the main file'
    





