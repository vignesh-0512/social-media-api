from .database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey # type: ignore
from sqlalchemy.sql.expression import null,text # type: ignore
from sqlalchemy.sql.sqltypes import TIMESTAMP # type: ignore
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='True',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    owner = relationship("User")

    

#orm model for user table
class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True,nullable=False)
    email = Column(String, nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    

 
