from creche.db.engine import DBSession
from creche.db.models import DBCreche

def create_creche(name: str, address: str, capacity: int):
    session = DBSession()
    new_creche = DBCreche(name=name, address=address, capacity=capacity)
    session.add(new_creche)
    session.commit()
    session.refresh(new_creche)
    return new_creche

def read_all_creches():
    session = DBSession()
    creches = session.query(DBCreche).all()
    return creches

def read_creche(id: int):
    session = DBSession()
    creche = session.query(DBCreche).get(id)
    return creche