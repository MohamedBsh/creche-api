from creche.db.operations.interface import DataObject
from creche.db.df_interface import DBInterface
from pydantic import BaseModel
from creche.db.operations.children import ChildCreateData
class ParentCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: str

def create_parent(parent_data: ParentCreateData, parent_interface: DBInterface) -> DataObject:
    return parent_interface.create(parent_data.model_dump())

def read_all_parents(parent_interface: DBInterface) -> list[DataObject]:
    return parent_interface.read_all()

def read_parent(id: int, parent_interface: DBInterface) -> DataObject:
    return parent_interface.read_by_id(id)

def delete_parent(id: int, parent_interface: DBInterface) -> DataObject:
    return parent_interface.delete(id)

def update_parent(id: int, first_name: str, last_name: str, email_address: str, phone_number: str, parent_interface: DBInterface) -> DataObject:
    return parent_interface.update(id, {"first_name": first_name, "last_name": last_name, "email_address": email_address, "phone_number": phone_number})

def add_child_to_parent(parent_id: int, child_interface: DBInterface, child_data: ChildCreateData, parent_interface: DBInterface) -> DataObject:
    parent = parent_interface.read_by_id(parent_id)  
    child_data['parent_id'] = parent_id
    child_data_object = child_interface.create(child_data.model_dump())
    parent.children.append(child_data_object)
    return parent_interface.update(parent_id, parent.model_dump())

def remove_child_from_parent(parent_id: int, child_id: int, parent_interface: DBInterface, child_interface: DBInterface) -> DataObject:
    parent = parent_interface.read_by_id(parent_id)
    child = child_interface.read_by_id(child_id)
    parent["child"] = None
    return parent_interface.update(parent_id, parent)

def get_children_of_parent(parent_id: int, parent_interface: DBInterface) -> list[DataObject]:
    parent = parent_interface.read_by_id(parent_id)
    return [child.model_dump() for child in parent.children]
