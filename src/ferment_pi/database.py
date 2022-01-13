import os
from datetime import datetime

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import JSON


BaseModel = declarative_base()

url = os.environ.get('DB_URL')

engine = create_engine(url, pool_pre_ping=True)

session_local = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_session():
    """Return DB Session Context."""

    try:
        session = session_local()
        yield session
    finally:
        session.close()


class Temperature(BaseModel):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    temperature = Column(String(5), nullable=False)
    humidity = Column(String(5), nullable=False)
    created_time = Column(DateTime, default=datetime.utcnow, nullable=False)


def save_temperature(temperature, humidity):
    with get_session() as session:
        try:
            batch = Temperature(temperature=temperature, humidity=humidity)

            session.add(batch)
            session.commit()
        except SQLAlchemyError as err:
            session.rollback()
            raise err
