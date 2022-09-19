from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from extentions import db


class Post:
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(UUID, db.ForeignKey('users.id'))
    body = db.Column(db.String(255))
    publish_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.body)
