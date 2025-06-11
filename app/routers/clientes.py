from fastapi import APIRouter
from ..dependencies import dep_session
from sqlmodel import SQLModel
from pydantic import EmailStr
from ..security.passwords import hash_password,verify_password
from datetime import date
from ..db.crud import select_rows,select_row,insert_row,update_row,delete_row
router = APIRouter(prefix='/clientes',tags={'clientes'})
from ..db.models import clientes



class ClientPublic (SQLModel):
    nombre:str
    telefono : str
    email : EmailStr
    fecha_registro: date

class ClientBase (SQLModel):
    nombre:str
    telefono : str
    password: str
    email : EmailStr


class ClientUpdate (SQLModel):
    nombre : str|None = None
    telefono : str|None = None
    password : str|None = None
    email : EmailStr|None = None
    
    
@router.get('',response_model=list[ClientPublic])
async def get_clients (session:dep_session):
    return select_rows(clientes,session)

@router.get('/{client_id}',response_model=ClientPublic)
async def get_client (client_id:int,session:dep_session):
    return select_row(clientes,client_id,session)

@router.post('')
async def new_client (client:ClientBase,session:dep_session):
    #Password hashed 
    client.password = hash_password(client.password)
    return insert_row(clientes,client,session)

@router.delete('/{client_id}')
async def delete_client(client_id:int,session:dep_session):
    delete_row(clientes,client_id,session)
    return {'message':'Client successfully deleted'}

@router.patch('/{client_id}',response_model=ClientPublic)
async def update_client (client_id:int,data_client:ClientUpdate,session:dep_session):
    if data_client.password is not None:
        data_client.password=hash_password(data_client.password)

    updated_client = update_row(clientes,client_id,data_client,session)
    return updated_client
