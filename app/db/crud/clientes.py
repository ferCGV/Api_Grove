from ..models import clientes
from sqlmodel import SQLModel,select


def create_client (client,session):
    new_client = clientes.model_validate(client)
    session.add(new_client)
    session.commit()
    session.refresh(new_client)
    return {'cliente':new_client}

def select_clients (session):
    return session.exec(select(clientes)).all()

def select_client(id,session):
    return session.get(clientes,id)
    
def delete_row (id,session):
    client = session.get(clientes,id)
    session.delete(client)
    session.commit()

def update_row(id,client_update,session):
    client = session.get(clientes,id)
    data_client = client_update.model_dump(exclude_unset=True)
    client.sqlmodel_update(data_client)
    session.add(client)
    session.commit()
    session.refresh(client)
    return client 

    