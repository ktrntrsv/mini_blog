from werkzeug.urls import url_parse

from flask_login import current_user, login_required, login_user, logout_user
from forms.sign_in_from import SignInForm
from forms.sign_up_form import SignUpForm
from models.user_model import User
from extentions import logger
from app import login_manager
from flask import (
    Flask,
    current_app,
    render_template,
    redirect,
    url_for,
    session,
    flash,
    request
)


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.query.get(user_id)


def sign_in():
    if current_user.is_authenticated:
        logger.info("Redirection for sign_in to me")
        return redirect(url_for("user_page", username=current_user.username))
    logger.info("Signing in")
    form = SignInForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', "warning")
            return redirect(url_for('sign_in'))
        login_user(user)
        return redirect(url_for("me"))
    return render_template('auth/sign_in.html', title='Sign In', form=form)


def sign_up():
    if current_user.is_authenticated:
        logger.info("Redirection for sign_up to me")
        return redirect(url_for('me'))
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        User.create_user(
            username=form.username.data,
            email=form.email.data,
            passwd=form.password.data
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("sign_in"))
    else:
        print(f"ERROR {form}")
    return render_template(url_for("sign_up"), form=form)


def log_out():
    logger.info("Logging out")
    logout_user()
    return redirect(url_for("sign_in"))
