from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv('DATABASE_URI')
engine = create_engine(uri)
meta = MetaData()
conn = engine.connect()