from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, dotenv_values
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import time

load_dotenv() 

SQL_ALCHEMY_DATABASE_URL = f'postgresql://postgres:{os.getenv('MY_PASS')}@localhost/fastapi'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#while True:
#    try:
#        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password=os.getenv('MY_PASS'), cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print("Database connection was successful!")
#        break
#    except Exception as error:
#        print("Connecting to database failed")
#        print("Error: ", error)
#        time.sleep(2)


