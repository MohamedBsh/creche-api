from pydantic import BaseModel
from creche.db.operations.interface import DataObject
from creche.db.db_interface import DBInterface

class CrecheCreateData(BaseModel):
    name: str
    address: str
    capacity: int

def create_creche(creche_data: CrecheCreateData, creche_interface: DBInterface) -> DataObject:
    return creche_interface.create(creche_data.model_dump())

def read_all_creches(creche_interface: DBInterface) -> list[DataObject]:
    return creche_interface.read_all()

def read_creche(id: int, creche_interface: DBInterface) -> DataObject:
    return creche_interface.read_by_id(id)
