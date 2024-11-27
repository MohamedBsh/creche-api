from datetime import date
from pydantic import BaseModel
from creche.db.operations.interface import DataObject
from creche.db.db_interface import DBInterface

class ChildCreateData(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    parent_id: int

def create_child(child_data: ChildCreateData, child_interface: DBInterface) -> DataObject:
    return child_interface.create(child_data.model_dump())

def read_all_children(child_interface: DBInterface) -> list[DataObject]:
    return child_interface.read_all()

def read_child(id: int, child_interface: DBInterface) -> DataObject:
    return child_interface.read_by_id(id)
