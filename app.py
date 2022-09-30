import secrets
import dotenv
from os import getenv
from flask_bootstrap import Bootstrap
from flask import Flask
from extentions import db, login_manager, moment
from routes import auth_views, other_views, posts_views, error_views, user_views


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
    login_manager.init_app(app)
    moment.init_app(app)


def add_url_rules(app):
    app.add_url_rule("/user/<username>/create_post/", view_func=posts_views.create_post, methods=("GET", "POST"))
    app.add_url_rule("/edit_post/<pos_id>/", view_func=posts_views.edit_post, methods=("GET", "POST"))
    app.add_url_rule("/delete_post/<post_id>/", view_func=posts_views.delete_post, methods=("GET", "POST"))

    app.add_url_rule("/sign_in/", view_func=auth_views.sign_in, methods=("GET", "POST"))
    app.add_url_rule("/sign_up/", view_func=auth_views.sign_up, methods=("GET", "POST"))
    app.add_url_rule("/log_out/", view_func=auth_views.log_out, )

    app.add_url_rule("/", view_func=other_views.root, )
    app.add_url_rule("/me/", view_func=user_views.me, methods=("GET", "POST"))
    app.add_url_rule("/user/<username>/edit_bio/", view_func=user_views.edit_bio, methods=("GET", "POST"))
    app.add_url_rule("/user/<username>", view_func=user_views.user_page, methods=("GET", "POST"))
    app.add_url_rule("/user/<username>/delete_user", view_func=user_views.delete_user)
    app.add_url_rule("/friends/", view_func=user_views.friends, )
    app.add_url_rule("/about/", view_func=other_views.about, )
    app.add_url_rule("/news/", view_func=posts_views.news, )
    app.register_error_handler(404, error_views.page_not_found, )
    app.register_error_handler(401, error_views.unauthorized, )


if __name__ == '__main__':
    create_app().run(debug=True)
