import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = os.getenv('DB_URI', default='mysql+mysqldb://root:root@localhost/software_doc_design')
engine = create_engine(url)
metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)
