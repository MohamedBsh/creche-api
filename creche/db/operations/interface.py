from typing import Any

DataObject = dict[str, Any]


class DataInterface:
    def read_by_id(self, id: int) -> DataObject:
        ...

    def read_all(self) -> list[DataObject]:
        ...

    def create(self, data: DataObject) -> DataObject:
        ...

    def update(self, id: int, data: DataObject) -> DataObject:
        ...

    def delete(self, id: int) -> DataObject:
        ...
