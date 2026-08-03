from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 

db_url = "your-postgres-connection-url"
engine = create_engine(db_url)
session = sessionmaker(bind= engine, autoflush= False)

