from fastapi import APIRouter
from ..dependencies import dep_session
from ..db.crud.clientes import create_client,select_clients,delete_row,update_row,select_client
from sqlmodel import SQLModel
from pydantic import EmailStr
from ..security.passwords import hash_password,verify_password
from datetime import date

router = APIRouter(prefix='/clientes',tags={'clientes'})



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
    return select_clients(session)

@router.get('/{id_client}',response_model=ClientPublic)
async def get_client (id_client:int,session:dep_session):
    return select_client(id_client,session)

@router.post('')
async def new_client (client:ClientBase,session:dep_session):
    #Password hashed 
    client.password = hash_password(client.password)
    return create_client(client,session)

@router.delete('/{id_client}')
async def delete_client(id_client:int,session:dep_session):
    delete_row(id_client,session)
    return {'message':'Client successfully deleted'}

@router.patch('/{id_client}',response_model=ClientPublic)
async def update_client (id_client:int,data_client:ClientUpdate,session:dep_session):
    updated_client = update_row(id_client,data_client,session)
    return updated_client
