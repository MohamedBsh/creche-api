from creche.db.engine import DBSession
from creche.db.models import DBParent, DBChild
from pydantic import BaseModel

class ParentCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: str

def create_parent(parent_data: ParentCreateData):
    session = DBSession()
    new_parent = DBParent(first_name=parent_data.first_name, last_name=parent_data.last_name, email_address=parent_data.email_address, phone_number=parent_data.phone_number)
    session.add(new_parent)
    session.commit()
    session.refresh(new_parent)
    return new_parent

def read_all_parents():
    session = DBSession()
    parents = session.query(DBParent).all()
    return parents

def read_parent(id: int):
    session = DBSession()
    parent = session.query(DBParent).get(id)
    return parent

def delete_parent(id: int):
    session = DBSession()
    parent = session.query(DBParent).get(id)
    session.delete(parent)
    session.commit()
    return parent

def update_parent(id: int, first_name: str, last_name: str, email_address: str, phone_number: str):
    session = DBSession()
    parent = session.query(DBParent).get(id)
    parent.first_name = first_name
    parent.last_name = last_name
    parent.email_address = email_address
    parent.phone_number = phone_number
    session.commit()
    return parent

def add_child_to_parent(parent_id: int, child_id: int):
    session = DBSession()
    parent = session.query(DBParent).get(parent_id)
    child = session.query(DBChild).get(child_id)
    parent.child = child
    session.commit()
    return parent

def remove_child_from_parent(parent_id: int, child_id: int):
    session = DBSession()
    parent = session.query(DBParent).get(parent_id)
    child = session.query(DBChild).get(child_id)
    parent.child = None
    session.commit()
    return parent

def get_children_of_parent(parent_id: int):
    session = DBSession()
    parent = session.query(DBParent).get(parent_id)
    return parent.children
