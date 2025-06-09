from sqlmodel import SQLModel,create_engine


#CONNECTION

sql_file_name = 'grove_database.db'
sql_url = f'sqlite:///{sql_file_name}'

connect_args ={'check_same_thread':False}
engine = create_engine(sql_url,connect_args=connect_args)

#FUNCTION }

def create_database ():
    SQLModel.metadata.create_all(engine)
    

