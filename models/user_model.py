from random import randint

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Table, Column, MetaData, Integer, Computed, String, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from extentions import db
from flask_login import UserMixin
from uuid import uuid1
from extentions import logger


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String, unique=True, nullable=False)
    passwd_hash = db.Column(String, nullable=False)
    bio = db.Column(String)
    avatar = db.Column(String)
    posts = db.relationship('Post', backref='author',  lazy='dynamic', primaryjoin="User.id == Post.author_id")

    def __init__(self, id_, username, email):
        self.id = id_
        self.username = username
        self.email = email
        self.passwd_hash = None
        self.bio = ""
        self.avatar = None
        self.posts = tuple()

    def __repr__(self):
        return f'<User {self.username!r}>'

    def set_password_hash(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd_hash, password)

    def set_avatar(self, icon="default"):
        if icon == "default":
            self.avatar = f"/static/avatars/default_avatar_{randint(1, 9)}.jpg"
            logger.info(f"Avatar have set for {self}")

    @classmethod
    def create_user(cls, username: str, email: str, passwd: str):
        user = cls(id_=str(uuid1()),
                   username=username.lower(),
                   email=email
                   )
        user.set_password_hash(passwd)
        user.set_avatar()
        db.session.add(user)
        db.session.commit()
        return user
