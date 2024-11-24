from fastapi import APIRouter, Body
from creche.db.operations.children import read_all_children, read_child, create_child
from datetime import date
router = APIRouter()

@router.get("/children")
def api_read_all_children():
    return read_all_children()

@router.post("/children")
def api_create_child(
    first_name: str = Body(...), 
    last_name: str = Body(...), 
    date_of_birth: date = Body(...), 
    parent_id: int = Body(...)
):
    return create_child(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, parent_id=parent_id)

@router.get("/children/{child_id}")
def api_read_child(child_id: int):
    return read_child(child_id)