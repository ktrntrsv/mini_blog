from flask import redirect, url_for, render_template, flash
from flask_login import current_user


def root():
    return redirect(url_for("sign_in"))


def me():
    return render_template("blog/me.html")


def about():
    return render_template("about.html")


def page_not_found(error):
    return render_template("404.html")


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
