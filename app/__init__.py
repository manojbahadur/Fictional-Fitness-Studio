from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .logger import setup_logger


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    setup_logger(app)
    
    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
