from fastapi import APIRouter, Body
from creche.db.operations.creches import read_all_creches, read_creche, create_creche

router = APIRouter()

@router.get("/creches")
def api_read_all_creches():
    return read_all_creches()

@router.post("/creches")
def api_create_creche(
    name: str = Body(...), 
    address: str = Body(...), 
    capacity: int = Body(...)
):
    return create_creche(name=name, address=address, capacity=capacity)

@router.get("/creches/{creche_id}")
def api_read_creche(creche_id: int):
    return read_creche(creche_id)