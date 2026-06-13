import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/superstore.db")

print(pd.read_sql("PRAGMA table_info(locations)", engine))