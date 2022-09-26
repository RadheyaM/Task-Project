import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# as we are hiding the env.py file it will not exist
# once the project is deployed to Heroku.
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes  # noqa
