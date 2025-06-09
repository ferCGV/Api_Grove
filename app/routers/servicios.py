from fastapi import APIRouter,Depends
from sqlmodel import Session,SQLModel,Field
from ..db.crud.servicios import read_services,create_service,delete_service,update_service
from ..dependencies import dep_session
from ..db.models import servicios

class ServiceBase (SQLModel):
    nombre : str
    precio : int

class UpdateService(SQLModel):
    nombre:str|None=None
    precio : int |None = None



router = APIRouter(prefix='/services',tags=['servicios'])

@router.get('',response_model=list[ServiceBase])
async def all_services (session:dep_session):
    return read_services(session)

@router.post('')
async def new_service (service:ServiceBase,session:dep_session):
    return create_service(service,session)

@router.delete('/service/{id_servicio}')
async def remove_service (id_servicio:int,session:dep_session):
    delete_service (id_servicio,session)
    return {'Status':'good'}

@router.patch('/service/{id_service}')
async def update (id_service : int,service:UpdateService,session:dep_session):
    return update_service(id_service,service,session)





