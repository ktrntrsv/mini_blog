from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Table, Column, MetaData, Integer, Computed, String, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from extentions import db
from flask_login import UserMixin
import sqlalchemy as sa
from uuid import uuid1
from extentions import logger


class UserDB(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String, unique=True, nullable=False)
    passwd_hash = db.Column(String, nullable=False)
    bio = db.Column(String)
    avatar = db.Column(String)

    def __init__(self, id, username, email, passwd_hash=None, bio=None, avatar=None):
        self.id = id
        self.username = username
        self.email = email
        self.passwd_hash = passwd_hash
        self.bio = bio
        self.avatar = avatar

    def __repr__(self):
        return f'<User {self.username!r}>'

    def set_password_hash(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd_hash, password)

    def set_icon(self, icon="default"):
        if icon == "default":
            self.avatar = "/static/avatars/default_avatar.png"
            logger.info(f"Avatar have set for {self}")

    @classmethod
    def create_user(cls, username: str, email: str, passwd: str):
        user = cls(id=str(uuid1()),
                   username=username,
                   email=email
                   )
        user.set_password_hash(passwd)
        user.set_icon()
        db.session.add(user)
        db.session.commit()
        print(f"Created user {user}")
        return user
