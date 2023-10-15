
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}/{settings.DB_DB}"

engine = create_engine(url=URL)

SessionLocal = sessionmaker(autoflush=False , autocommit=False , bind=engine)
    
Base = declarative_base()

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
