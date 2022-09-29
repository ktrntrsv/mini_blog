from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from extentions import db, logger
from models.user_model import User


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(UUID, db.ForeignKey('users.id'), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    publish_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, author_id, body):
        self.author_id = author_id
        self.body = body

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    @classmethod
    def create_post(cls, author_id: User, body: str):
        post = cls(
            author_id=author_id,
            body=body,
        )
        db.session.add(post)
        db.session.commit()
        logger.info(f"Created post {post.id}")
        return post

