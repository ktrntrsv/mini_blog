from datetime import datetime

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

from extentions import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    publish_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, post_id, author_id, body, publish_time):
        self.id = post_id
        self.author_id = author_id
        self.body = body
        self.publish_time = publish_time

    def __repr__(self):
        return '<Post {}>'.format(self.body)
