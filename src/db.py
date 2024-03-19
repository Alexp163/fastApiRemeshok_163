from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(engine)
Base = declarative_base()
print(Base.metadata)