from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from creche.db.models import Base

engine: Engine = None
DBSession = sessionmaker()


def init_db(file: str):
    global engine
    engine = create_engine(file)
    Base.metadata.create_all(engine)
    DBSession.configure(bind=engine)
