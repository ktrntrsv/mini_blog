import views.posts
from views import auth

import secrets
import dotenv
from os import getenv
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dotenv.load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"postgresql://{getenv('PG_USER')}:{getenv('PG_PASSWORD')}@localhost:{getenv('PORT')}/blog"
db = SQLAlchemy(app)
from models.user import UserDB

Bootstrap(app)

secret = secrets.token_urlsafe(32)
app.secret_key = secret

redirect(url_for("sign_in"))


@app.route("/me", methods=("GET", "POST"))
def me():
    return render_template("blog/me.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


def sign_in():
    return render_template("auth/sign_in.html")


def sign_up():
    if request.method == "POST":
        print("POST HERE")
        form = request.form

        email = form["email"]
        username = form["username"]
        password_1 = form["passwd_1"]
        password_2 = form["passwd_2"]
        # todo set checkers
        db

        # conn = config.get_db_connection()
        # cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        # cursor.execute("INSERT INTO users VALUES (%s, %s)", (first_name, last_name, email,))
        flash(f"Ok, you have added", category="success")
        # conn.commit()
        return render_template("auth/sign_in.html")

    return render_template("auth/sign_up.html")


def is_valid_data(name, age) -> bool:
    valid_data = True

    if not name or not age:
        flash(f"All fields are required.", category="warning")
        valid_data = False
    if not isinstance(name, str):
        flash(f"Name should be string type.", category="warning")
        valid_data = False
    if not age.isdigit():
        flash(f"Age should be integer type.", category="warning")
        valid_data = False

    return valid_data


def log_out():
    return render_template("auth/log_out.html")


app.add_url_rule("/post", view_func=views.posts.post)
app.add_url_rule("/edit_post", view_func=views.posts.edit_post, methods=("GET", "POST"))
app.add_url_rule("/delete_post", view_func=views.posts.delete_post, methods=("GET", "POST"))

# app.add_url_rule("/sign_in", view_func=sign_in_up_out.sign_in, methods=("GET", "POST"))
# app.add_url_rule("/sign_up", view_func=sign_in_up_out.sign_up, methods=("GET", "POST"))
# app.add_url_rule("/log_out", view_func=sign_in_up_out.log_out, )

if __name__ == '__main__':
    app.run()
