import os
import uuid

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy.dialects.postgresql import UUID as UUIDType




loaded = load_dotenv('.env.development')


engine = create_engine(f'postgresql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}')

# Create a scoped database session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create a base class for declarative models
Base = declarative_base()
Base.query = db_session.query_property()

# Initialize the database schema
def init_db():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


class Model(Base):
    __abstract__ = True

    id = Column(UUIDType(), primary_key=True, default=uuid.uuid4)
