from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class PosgresBlogs(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key= True)
    title = Column(String)
    content = Column(String)

