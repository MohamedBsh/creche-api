from fastapi import APIRouter
from creche.db.operations.children import read_all_children, read_child, create_child
from creche.db.operations.children import ChildCreateData
from creche.db.db_interface import DBInterface
from creche.db.models import DBChild

router = APIRouter()

@router.get("/children")
def api_read_all_children():
    child_interface = DBInterface(DBChild)
    return read_all_children(child_interface)

@router.post("/children")
def api_create_child(
    child: ChildCreateData
):
    child_interface = DBInterface(DBChild)
    return create_child(child, child_interface)

@router.get("/children/{child_id}")
def api_read_child(child_id: int):
    child_interface = DBInterface(DBChild)
    return read_child(child_id, child_interface)
