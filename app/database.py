from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import Settings
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()  #creating a base class every model will be extending this


#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database="ecommerce",user="postgres",password="12345",cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break

#     except Exception as error:
#         print("Connection failed")
#         print("Error:", error)
#         time.sleep(2)
