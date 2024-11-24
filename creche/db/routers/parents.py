from fastapi import APIRouter, Body
from creche.db.operations.parents import read_all_parents, read_parent, create_parent, delete_parent, update_parent, add_child_to_parent, remove_child_from_parent, get_children_of_parent
router = APIRouter()

@router.get("/parents")
def api_read_all_parents():
    return read_all_parents()

@router.post("/parents")
def api_create_parent(
    first_name: str = Body(...), 
    last_name: str = Body(...), 
    email_address: str = Body(...), 
    phone_number: str = Body(...),
    parent_id: int = Body(...)
):
    return create_parent(first_name=first_name, last_name=last_name, email_address=email_address, phone_number=phone_number)

@router.get("/parents/{parent_id}")
def api_read_parent(parent_id: int):
    return read_parent(parent_id)

@router.delete("/parents/{parent_id}")
def api_delete_parent(parent_id: int):
    return delete_parent(parent_id)

@router.put("/parents/{parent_id}")
def api_update_parent(parent_id: int, first_name: str, last_name: str, email_address: str, phone_number: str):
    return update_parent(parent_id, first_name, last_name, email_address, phone_number)

@router.post("/parents/{parent_id}/children")
def api_add_child_to_parent(parent_id: int, child_id: int):
    return add_child_to_parent(parent_id, child_id)

@router.delete("/parents/{parent_id}/children/{child_id}")
def api_remove_child_from_parent(parent_id: int, child_id: int):
    return remove_child_from_parent(parent_id, child_id)

@router.get("/parents/{parent_id}/children")
def api_get_children_of_parent(parent_id: int):
    return get_children_of_parent(parent_id)
