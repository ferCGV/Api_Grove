from sqlmodel import Session,select
from ..models import servicios

#CREATE A SERVICE
def create_service(service,session):
    newservice = servicios.model_validate(service)
    session.add(newservice)
    session.commit()
    session.refresh(newservice)
    return f'El servicio se agreo correctamente : {service}'


#READ SERVICES
def read_services(session):
    services = session.exec(select(servicios)).all()
    return services
    

#DELETE A SERVICE
def delete_service(id,session):
    service = session.get(servicios,id)
    session.delete(service)
    session.commit()
    

#UPDATE A SERVICE
def update_service(id,service_update,session):
    service = session.get(servicios,id)
    new_data =service_update.model_dump(exclude_unset=True)
    service_update =service.sqlmodel_update(new_data)
    session.add(service_update)
    session.commit()
    session.refresh(service)
    return {'message':'felicidades bro'}


