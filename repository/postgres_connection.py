from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 

db_url = "postgresql://postgres:ash123@localhost:5432/bitfumes"
engine = create_engine(db_url)
session = sessionmaker(bind= engine, autoflush= False)

