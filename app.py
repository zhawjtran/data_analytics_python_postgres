import os
from datetime import datetime

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


app = Flask(__name__, static_folder='static')

load_dotenv()

#app.config.update(
#    SQLALCHEMY_DATABASE_URI=f"postgresql://{os.getenv('DBUSER')}:{os.getenv('DBPASS')}@{os.getenv('DBHOST')}/{os.getenv('DBNAME')}",
#    SQLALCHEMY_TRACK_MODIFICATIONS=False,
#)

app.config.update(
    SQLALCHEMY_DATABASE_URI=f"postgresql://{os.getenv('DBUSER')}:{os.getenv('DBPASS')}@{os.getenv('DBHOST')}/{os.getenv('DBNAME')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

#app.config.update(
#    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
#    SQLALCHEMY_TRACK_MODIFICATIONS=False,
#)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
