# setup for database testing
from models import *
from config import Paths
db.bind('sqlite', Paths.DB_PATH, create_db=True)
db.generate_mapping()
