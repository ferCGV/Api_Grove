
from sqlmodel import select

def insert_row (table,row,session):
    row = table.model_validate(row)
    session.add(row)
    session.commit()
    session.refresh(row)
    return {'message':row}

def select_rows (table,session):
    return session.exec(select(table)).all()

def select_row(table,id,session):
    return session.get(table,id)
    
def delete_row (table,id,session):
    row = session.get(table,id)
    session.delete(row)
    session.commit()

def update_row(table,id,updated_row,session):
    row = session.get(table,id)
    data_row = updated_row.model_dump(exclude_unset=True)
    row.sqlmodel_update(data_row)
    session.add(row)
    session.commit()
    session.refresh(row)
    return row 