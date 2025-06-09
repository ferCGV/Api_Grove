from .db.session import get_session
from typing import Annotated
from sqlmodel import Session
from fastapi import Depends

dep_session = Annotated[Session,Depends(get_session)]