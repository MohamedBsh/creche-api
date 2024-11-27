from fastapi import APIRouter
from creche.db.operations.creches import read_all_creches, read_creche, create_creche
from creche.db.operations.creches import CrecheCreateData
from creche.db.df_interface import DBInterface
from creche.db.models import DBCreche

router = APIRouter()

@router.get("/creches")
def api_read_all_creches():
    creche_interface = DBInterface(DBCreche)
    return read_all_creches(creche_interface)

@router.post("/creches")
def api_create_creche(
    creche: CrecheCreateData
):
    creche_interface = DBInterface(DBCreche)
    return create_creche(creche, creche_interface)

@router.get("/creches/{creche_id}")
def api_read_creche(creche_id: int):
    creche_interface = DBInterface(DBCreche)
    return read_creche(creche_id, creche_interface)
