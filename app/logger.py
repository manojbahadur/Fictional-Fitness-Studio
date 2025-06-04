import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(app):
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)  # Make sure the logs folder is created

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )

    # Info Logger
    info_handler = RotatingFileHandler(f'{log_dir}/info.log', maxBytes=100000, backupCount=3)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    # Error Logger
    error_handler = RotatingFileHandler(f'{log_dir}/error.log', maxBytes=100000, backupCount=3)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # Attach both handlers
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(info_handler)
    app.logger.addHandler(error_handler)

    app.logger.info('🚀 Logger initialized and app started')
