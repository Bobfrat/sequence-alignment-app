from flask import Flask
from flask_session import Session
from flask_bootstrap import Bootstrap
from celery import Celery
from config import config, Config

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    Bootstrap(app)
    # Session(app)
    celery.conf.update(app.config)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
