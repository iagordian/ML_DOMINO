from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    '''Создание объекта сессии'''
    db = SessionLocal()
    return db

def get_connect():
    '''Создание соединения'''

    connect = engine.connect()
    return connect



class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
     'ix': "'ix_%(column_0_label)s'", 
     'uq': "'uq_%(table_name)s_%(column_0_name)s'", 
     'ck': "'ck_%(table_name)s_`%(constraint_name)s`'", 
     'fk': "'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'", 
     'pk': "'pk_%(table_name)s'"}
    )