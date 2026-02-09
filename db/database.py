from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://user:password@localhost/ai_app"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
