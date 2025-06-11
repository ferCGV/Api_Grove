from fastapi import APIRouter,Depends
from sqlmodel import Session,SQLModel,Field
from ..db.crud import select_rows,insert_row,update_row,delete_row,select_row
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
    return select_rows(servicios,session)

@router.post('')
async def new_service (service:ServiceBase,session:dep_session):
    return insert_row(servicios,service,session)

@router.delete('/service/{service_id}')
async def remove_service (service_id:int,session:dep_session):
    delete_row (servicios,service_id,session)
    return {'Status':'good'}

@router.patch('/service/{service_id}')
async def update (service_id : int,service:UpdateService,session:dep_session):
    return update_row(servicios,service_id,service,session)

@router.get('/{service_id}')
async def get_service (service_id,session:dep_session):
    select_row(servicios,service_id,session)





