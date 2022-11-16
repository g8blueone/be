from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.secret_key = 'thisisasecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HEALTH.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    database.init_app(app)
    migrate.init_app(app)
    bcrypt.init_app(app)

    return app
