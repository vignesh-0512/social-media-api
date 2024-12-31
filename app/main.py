from fastapi import FastAPI # type: ignore
import psycopg2 # type: ignore
from psycopg2.extras import RealDictCursor # type: ignore
import time  
from fastapi import Response,Depends # type: ignore
from .import models
from .database import engine
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


# #decorator - when added decorator to function it perform path operation
# # @app.get("/hello")  
# #async optional
# def root():
#     return{"message":"Hello"}

# @app.get("/posts",response_model=List[schema.Post])
# def get_posts(db:Session=Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts
 
# @app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
# def create_post(post:schema.PostCreate,db:Session=Depends(get_db)):
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post
   

# @app.get("/posts/{id}",response_model=schema.Post)
# def get_post(id:int,db:Session=Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
#     return post


# @app.delete("/posts/{id}",response_model=schema.Post )
# def delete_post(id:int, db:Session=Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id)
 
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
#     post.delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

  
# @app.put("/posts/{id}")
# def update_post(id:int,updated_post:schema.Post,db:Session = Depends(get_db)):
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()
   
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} not found")
#     post_query.update(updated_post.dict(),synchronize_session=False)
#     db.commit()
#     return {"data":post_query.first()}


# #user side activities
# @app.post("/user",status_code=status.HTTP_201_CREATED,response_model=schema.UserOut)
# def create_user(user:schema.UserCreate, db:Session = Depends(get_db)):
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}",response_model=schema.UserOut)
# def get_user(id:int, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"User with id:{id} does not exist")

#     return user

