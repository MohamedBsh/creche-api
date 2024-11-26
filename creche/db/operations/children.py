from creche.db.engine import DBSession
from creche.db.models import DBChild
from datetime import date
from pydantic import BaseModel

class ChildCreateData(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    parent_id: int

def create_child(child_data: ChildCreateData):
    session = DBSession()
    new_child = DBChild(**child_data.model_dump())
    session.add(new_child)
    session.commit()
    return new_child

def read_all_children():
    session = DBSession()
    children = session.query(DBChild).all()
    return children

def read_child(id: int):
    session = DBSession()
    child = session.query(DBChild).get(id)
    return child