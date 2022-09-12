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

    id = db.Column(UUID, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String, unique=True, nullable=False)
    passwd_hash = db.Column(String, nullable=False)
    bio = db.Column(String)
    avatar = db.Column(LargeBinary)

    def __repr__(self):
        return f'<User {self.username!r}>'

    def set_password_hash(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd_hash, password)

    @classmethod
    def create_user(cls, username: str, email: str, passwd: str):
        user = cls(user_id=str(uuid1()),
                   username=username,
                   email=email
                   )
        user.set_password_hash(passwd)
        db.session.add(user)
        db.session.commit()
        print(f"Created user {user}")
        return user
