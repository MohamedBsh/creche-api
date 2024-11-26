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
    new_child = DBChild(first_name=child_data.first_name, last_name=child_data.last_name, date_of_birth=child_data.date_of_birth, parent_id=child_data.parent_id)
    session.add(new_child)
    session.commit()
    session.refresh(new_child)
    return new_child

def read_all_children():
    session = DBSession()
    children = session.query(DBChild).all()
    return children

def read_child(id: int):
    session = DBSession()
    child = session.query(DBChild).get(id)
    return child