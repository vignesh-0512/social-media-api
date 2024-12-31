from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter # type: ignore
from ..import models,schema,oauth
from sqlalchemy.orm import Session # type: ignore
from ..database import engine,get_db
from typing import Optional,List

router = APIRouter(
    prefix = "/posts",
    tags=["posts"]
)
#decorator - when added decorator to function it perform path operation
# @app.get("/hello")  
#async optional
def root():
    return{"message":"Hello"}

@router.get("/",response_model=List[schema.Post])
def get_posts(db:Session=Depends(get_db),current_user:int=Depends(oauth.get_current_user),limit:int=10):
    posts = db.query(models.Post).limit(limit).all()
    return posts
 
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.Post)
def create_post(post:schema.PostCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth.get_current_user)):
    new_post = models.Post(owner_id=current_user.id ,**post.dict())
    print(current_user.email)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
   

@router.get("/{id}",response_model=schema.Post)
def get_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
    return post


@router.delete("/{id}",response_model=schema.Post )
def delete_post(id:int, db:Session=Depends(get_db),current_user:int=Depends(oauth.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    
    if post.owner_id != oauth.get_current_user:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail="Not authorized")

    post_query.delete(synchronize_session=False)
    db.commit()
  
@router.put("/{id}")
def update_post(id:int,updated_post:schema.Post,db:Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
   
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} not found")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return {"data":post_query.first()}

    if post.owner_id != oauth.get_current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail="Not authorized")
  

