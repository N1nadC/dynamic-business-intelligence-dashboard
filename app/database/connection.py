from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/superstore.db"

engine = create_engine(DATABASE_URL)