from pydantic import BaseModel
from creche.db.operations.interface import DataObject
from creche.db.df_interface import DBInterface

class CaregiverCreateData(BaseModel):
    first_name: str
    last_name: str
    qualifications: str
    years_of_experience: int
    caregiver_email_address: str
    caregiver_phone_number: str

def create_caregiver(caregiver_data: CaregiverCreateData, caregiver_interface: DBInterface) -> DataObject:
    return caregiver_interface.create(caregiver_data.model_dump())

def read_all_caregivers(caregiver_interface: DBInterface) -> list[DataObject]:
    return caregiver_interface.read_all()

def read_caregiver(id: int, caregiver_interface: DBInterface) -> DataObject:
    return caregiver_interface.read_by_id(id)
