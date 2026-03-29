from fastapi import APIRouter , Depends
from data.exampledata import blogs
from schema.pydantic_schema import BlogCreate
from schema.postgres_schema import Base , PosgresBlogs
from repository.postgres_connection import engine, session
from sqlalchemy.orm import Session

router = APIRouter() 

Base.metadata.create_all(engine)

def init_db():
    try:
        db = session()
        yield db
    except Exception as e:
        return f"An Error has Occurred {e}"
    finally:
        db.close()

def create_db():
    db = session()

    counter = db.query(PosgresBlogs).count()
    if counter == 0:
        for blog in blogs:
            db.add(PosgresBlogs(**blog))
        
        db.commit()

create_db()

@router.get("/",include_in_schema=False)
def homepage():
    return "Welcome To FastAPI"

@router.get("/all/blogs")
def all_blogs(db : Session = Depends(init_db)):
    db_products = db.query(PosgresBlogs).all()
    return db_products

@router.get("/get/blogs/{id}")
def get_blog_id(id : int, db : Session = Depends(init_db)):
    db_products = db.query(PosgresBlogs).filter(PosgresBlogs.id == id).first()
    if db_products:
        return db_products
    else:
        return {"detail" : "No Blog Found By The ID!"}

    
@router.post("/create/blog")
def create_blog(blog : BlogCreate, db : Session = Depends(init_db)):
    db.add(PosgresBlogs(**blog.model_dump()))
    db.commit()
    return {"detail" : "Blog Added Successfully!"}

@router.put("/update/blog")
def update_blog(id : int, updateblog : BlogCreate, db : Session = Depends(init_db)):
    db_products = db.query(PosgresBlogs).filter(PosgresBlogs.id == id).first()
    if db_products:
        db_products.title = updateblog.title
        db_products.content = updateblog.content
        db.commit()
        return {"detail" : "Updated Blog Successfully!"}
    else:
        return {"detail" : "No Blog Found!"}
    
@router.delete("/delete/blog")
def delete_blog(id : int, db : Session = Depends(init_db)):
    db_products = db.query(PosgresBlogs).filter(PosgresBlogs.id == id).first()
    if db_products:
        db.delete(db_products)
        db.commit()
        return {"detail" : "Deleted Blog Successfully!"}
    
