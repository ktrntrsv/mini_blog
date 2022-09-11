import secrets
import dotenv
from os import getenv
from flask_bootstrap import Bootstrap
from flask import Flask
from extentions import db
from views import auth, other, posts


def create_app():
    app = Flask(__name__)

    dotenv.load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f"postgresql://{getenv('PG_USER')}:{getenv('PG_PASSWORD')}@localhost:{getenv('PORT')}/blog"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Bootstrap(app)
    app.secret_key = secrets.token_urlsafe(32)
    register_extensions(app)
    add_url_rules(app)
    return app


def register_extensions(app):
    db.init_app(app)


def add_url_rules(app):
    app.add_url_rule("/post", view_func=posts.post)
    app.add_url_rule("/edit_post", view_func=posts.edit_post, methods=("GET", "POST"))
    app.add_url_rule("/delete_post", view_func=posts.delete_post, methods=("GET", "POST"))

    app.add_url_rule("/sign_in", view_func=auth.sign_in, methods=("GET", "POST"))
    app.add_url_rule("/sign_up", view_func=auth.sign_up, methods=("GET", "POST"))
    app.add_url_rule("/log_out", view_func=auth.log_out, )

    app.add_url_rule("/", view_func=other.root, )
    app.add_url_rule("/me", view_func=other.me, methods=("GET", "POST"))
    app.add_url_rule("/about", view_func=other.about, )
    app.register_error_handler(404, other.page_not_found, )


if __name__ == '__main__':
    create_app().run()
