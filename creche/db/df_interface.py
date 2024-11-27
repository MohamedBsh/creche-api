from typing import Any
from creche.db.models import Base
from creche.db.engine import DBSession

DataObject = dict[str, Any]

class DBInterface:
    def __init__(self, db_class: type(Base)):
        self.db_class = db_class

    def read_by_id(self, id: int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        return result.model_dump()
    
    def read_all(self) -> list[DataObject]:
        session = DBSession()
        results = session.query(self.db_class).all()
        return [result.model_dump() for result in results]
    
    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        new_result = self.db_class(**data)
        session.add(new_result)
        session.commit()
        return new_result.model_dump()
    
    def update(self, id: int, data: DataObject) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        for key, value in data.items():
            setattr(result, key, value)
        session.commit()
        return result.model_dump()
    
    def delete(self, id : int) -> DataObject:
        session = DBSession()
        result = session.query(self.db_class).get(id)
        session.delete(result)
        session.commit()
        return result.model_dump()