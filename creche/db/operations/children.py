from creche.db.engine import DBSession
from creche.db.models import DBChild
from datetime import date

def create_child(first_name: str, last_name: str, date_of_birth: date, parent_email_address: str, parent_phone_number: str):
    session = DBSession()
    new_child = DBChild(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, parent_email_address=parent_email_address, parent_phone_number=parent_phone_number)
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