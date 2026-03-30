from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 

db_url = "postgresql://postgres:ash123@my-postgres:5433/bitfumes"
engine = create_engine(db_url)
session = sessionmaker(bind= engine, autoflush= False)

