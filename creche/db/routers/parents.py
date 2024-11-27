from fastapi import APIRouter
from creche.db.operations.parents import read_all_parents, read_parent, create_parent, delete_parent, update_parent, add_child_to_parent, remove_child_from_parent, get_children_of_parent
from creche.db.operations.parents import ParentCreateData
from creche.db.db_interface import DBInterface
from creche.db.models import DBParent

router = APIRouter()

@router.get("/parents")
def api_read_all_parents():
    return read_all_parents()

@router.post("/parents")
def api_create_parent(
    parent: ParentCreateData
):  
    parent_interface = DBInterface(DBParent)
    return create_parent(parent, parent_interface)

@router.get("/parents/{parent_id}")     
def api_read_parent(parent_id: int):
    parent_interface = DBInterface(DBParent)
    return read_parent(parent_id, parent_interface)

@router.delete("/parents/{parent_id}")
def api_delete_parent(parent_id: int):
    parent_interface = DBInterface(DBParent)
    return delete_parent(parent_id, parent_interface)

@router.put("/parents/{parent_id}")
def api_update_parent(parent_id: int, parent: ParentCreateData):
    parent_interface = DBInterface(DBParent)
    return update_parent(parent_id, parent, parent_interface)

@router.post("/parents/{parent_id}/children")
def api_add_child_to_parent(parent_id: int, child_id: int):
    parent_interface = DBInterface(DBParent)
    return add_child_to_parent(parent_id, child_id, parent_interface)

@router.delete("/parents/{parent_id}/children/{child_id}")
def api_remove_child_from_parent(parent_id: int, child_id: int):
    parent_interface = DBInterface(DBParent)
    return remove_child_from_parent(parent_id, child_id, parent_interface)

@router.get("/parents/{parent_id}/children")
def api_get_children_of_parent(parent_id: int):
    parent_interface = DBInterface(DBParent)
    return get_children_of_parent(parent_id, parent_interface)
