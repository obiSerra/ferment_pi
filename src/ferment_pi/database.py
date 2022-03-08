import os
import sys
from contextlib import contextmanager
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

BaseModel = declarative_base()

url = os.environ.get(
    'DB_URL', 'postgresql://testuser:testsecretpassword@fermentpi_db:5432/testdatabase')
print(url)
if url is None:
    print("ERROR missing DB_URL env")
    sys.exit(1)

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


def get_last_temperature():
    with get_session() as session:
        try:
            obj = session.query(Temperature).order_by(
                Temperature.created_time.desc()).first()
            if obj is None:
                return None
            return {'id': obj.id, 'temperature': obj.temperature,
                    'humidity': obj.humidity, 'date': obj.created_time}
        except SQLAlchemyError as err:
            session.rollback()
            raise err
