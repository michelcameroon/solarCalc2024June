from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)

app.app_context().push()

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#from models import Project
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
