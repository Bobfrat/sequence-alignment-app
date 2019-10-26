# Configuration
import logging
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_5#y2L"F4Q8znxec]/'
    SESSION_TYPE = 'redis'
    HOST = '0.0.0.0'
    PORT = '3000'
    # Logging
    LOGGING = True
    LOG_LEVEL = 'INFO'
    LOG_FILE_PATH = 'logs/'
    LOG_FILE = 'app.log'
    
    WTF_CSRF_ENABLED = True
    SSL_DISABLE = False
    
    # Celery
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


    @staticmethod
    def init_app(app):
        logging_level = getattr(logging, app.config.get('LOG_LEVEL', 'DEBUG'))

        formatter = logging.Formatter('%(asctime)s - %(process)d - %(name)s - %(module)s:'
                                      '%(lineno)d - %(levelname)s - %(message)s')

        log_directory = app.config.get('LOG_FILE_PATH')
        log_file = app.config.get('LOG_FILE')
        if log_directory and log_file:
            log_filename = os.path.join(log_directory, app.config['LOG_FILE'])
            if not os.path.exists(os.path.dirname(log_filename)):
                os.makedirs(os.path.dirname(log_filename))
            file_handler = logging.FileHandler(log_filename, mode='a+')
            file_handler.setFormatter(formatter)
            app.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        app.logger.setLevel(logging_level)
        app.logger.info('Application Process Started')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}