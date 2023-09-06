from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = "sqlite:///myrestaurant.db" 
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

Base = declarative_base()
