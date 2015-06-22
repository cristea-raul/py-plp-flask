from flask import Flask

from config import Paths

# init
app = Flask(__name__)
app.config.from_object(__name__)

from views import *
from models import *

if __name__ == '__main__':
    # database setup
    db.bind('sqlite', Paths.DB_PATH, create_db=True)
    db.generate_mapping(create_tables=True)

    app.run()
