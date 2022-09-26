from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from loguru import logger
from flask_moment import Moment


db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()


logger.add('logs.log', encoding="utf8", rotation='15 MB', compression='zip', level="DEBUG")
logger.add('logs.log', encoding="utf8", rotation='15 MB', compression='zip', level="INFO")
