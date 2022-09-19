from flask import redirect, url_for, render_template, flash


def root():
    return redirect(url_for("sign_in"))


def about():
    return render_template("about.html")


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
