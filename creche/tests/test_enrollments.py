import unittest
from creche.db.operations.enrollments import EnrollmentCreateData
from creche.db.df_interface import DBInterface
from creche.db.models import DBEnrollment
from datetime import date, timedelta
from creche.db.models import DataObject
from creche.db.operations.enrollments import create_enrollment

class DataInterfaceStub:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError
    def read_all(self) -> list[DataObject]:
        raise NotImplementedError       
    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError
    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError
    def delete(self, id: int) -> DataObject:
        raise NotImplementedError

class CrecheInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "name": "Creche 1", "address": "123 Main St", "capacity": 10, "price": 100}

class ChildInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "first_name": "John", "last_name": "Doe", "date_of_birth": date.today()}

class CaregiverInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "first_name": "Jane", "last_name": "Doe", "qualifications": "Bachelor's Degree in Early Childhood Education", "years_of_experience": 5, "caregiver_email_address": "jane.doe@example.com", "caregiver_phone_number": "123-456-7890"}

class EnrollmentInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        enrollment = dict(data)
        enrollment["id"] = 1
        return enrollment

class TestEnrollments(unittest.TestCase):
    def test_price_one_day(self):
        enrollment_interface = DBInterface(DBEnrollment)
        enrollment_data = EnrollmentCreateData(
            start_date=date.today(),
            end_date=date.today() + timedelta(days=1)
        )
        enrollment = create_enrollment(enrollment_data, enrollment_interface, ChildInterface(), CaregiverInterface(), CrecheInterface())
        self.assertEqual(enrollment["price"], 100)
