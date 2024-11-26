from creche.db.engine import DBSession
from creche.db.models import DBCreche
from pydantic import BaseModel

class CrecheCreateData(BaseModel):
    name: str
    address: str
    capacity: int

def create_creche(creche_data: CrecheCreateData):
    session = DBSession()
    new_creche = DBCreche(**creche_data.model_dump())
    session.add(new_creche)
    session.commit()
    return new_creche

def read_all_creches():
    session = DBSession()
    creches = session.query(DBCreche).all()
    return creches

def read_creche(id: int):
    session = DBSession()
    creche = session.query(DBCreche).get(id)
    return creche