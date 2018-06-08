from model.models import CreateDatabase
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=CreateDatabase.engine)
session = Session()
