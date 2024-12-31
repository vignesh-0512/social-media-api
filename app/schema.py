from pydantic import BaseModel # type: ignore
from datetime import datetime
from typing import Optional
#model developed using pydantic

class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email:str
    password:str

class UserOut(BaseModel):
    id:int
    email:str
    created_at:datetime

    class Config:
        orm_mode = True  

class UserLogin(BaseModel):
    email:str
    password:str


class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:Optional[int] = None
