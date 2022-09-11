from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Table, Column, MetaData, Integer, Computed, String, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from extentions import db
from flask_login import UserMixin
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid1


class UserDB(UserMixin, db.Model):
    __tablename__ = 'users'

    user_id = sa.Column(UUID, primary_key=True)
    username = sa.Column(String, unique=True, nullable=False)
    email = sa.Column(String, unique=True, nullable=False)
    passwd_hash = sa.Column(String, nullable=False)
    bio = sa.Column(String)
    avatar = sa.Column(LargeBinary)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password_hash(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd_hash, password)

    def add_new_user(self):
        pass
