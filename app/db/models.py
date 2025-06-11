from sqlmodel import SQLModel,Field
from pydantic import EmailStr
from datetime import date

class clientes (SQLModel,table=True):
    id : int =Field (default=None,primary_key=True) 
    nombre : str =Field(index=True)
    password : str = Field(index=True)
    telefono :str =Field(index=True,max_length=10,min_length=10)
    email : EmailStr = Field(index=True)
    fecha_registro : date = Field(index=True,default_factory=date.today)

class servicios (SQLModel,table=True):
    id : int = Field(default=None,primary_key=True)
    nombre : str= Field (index=True)
    precio : int = Field(index=True)

class barberos (SQLModel,table=True):
    id : int = Field(default=None,primary_key=True)
    nombre: str =Field(index=True)
    sueldo : int =Field(index=True)
    telefono : str =Field(index=True)
    email : EmailStr=Field(index=True)








    