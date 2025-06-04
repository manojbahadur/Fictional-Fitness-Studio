from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .logger import setup_logger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    setup_logger(app)
    db.init_app(app)

    app_api = Api(app, doc='/docs', title="🏋️ Fitness Studio Booking API", version="1.0")

    # 👇 Lazy import to prevent circular dependency
    from .routes import api
    app_api.add_namespace(api, path='/')

    return app

