from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class DBChild(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)

    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=False)
    parent = relationship("DBParent", back_populates="children")


class DBParent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    children = relationship("DBChild", back_populates="parent")


class DBCaregiver(Base):
    __tablename__ = "caregiver"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    qualifications = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    caregiver_email_address = Column(String, nullable=False)
    caregiver_phone_number = Column(String, nullable=False)


class DBCreche(Base):
    __tablename__ = "creche"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


class DBEnrollment(Base):
    __tablename__ = "enrollment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)

    child_id = Column(Integer, ForeignKey("child.id"), nullable=False)
    child = relationship("DBChild")
    caregiver_id = Column(Integer, ForeignKey("caregiver.id"), nullable=False)
    caregiver = relationship("DBCaregiver")
    creche_id = Column(Integer, ForeignKey("creche.id"), nullable=False)
    creche = relationship("DBCreche")
    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=False)
    parent = relationship("DBParent")
