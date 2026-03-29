from pydantic import BaseModel

class BlogCreate(BaseModel):
    id : int 
    title : str 
    content : str 

