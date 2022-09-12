from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from loguru import logger

db = SQLAlchemy()
login_manager = LoginManager()

logger.add('logs.log', encoding="utf8", rotation='15 MB', compression='zip', level="DEBUG")
logger.add('logs.log', encoding="utf8", rotation='15 MB', compression='zip', level="INFO")
