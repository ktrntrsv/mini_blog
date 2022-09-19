from werkzeug.urls import url_parse

from flask_login import current_user, login_required, login_user, logout_user
from forms.sign_in_from import SignInForm
from forms.sign_up_form import SignUpForm
from models.user_model import UserDB
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
    logger.info(f"In load_manager")
    return UserDB.query.get(user_id)


def sign_in():
    if current_user.is_authenticated:
        logger.info("Redirection for sign_in to me")
        return redirect(url_for(f'/user/{current_user.username}'))
    logger.info("Signing in")
    form = SignInForm(request.form)
    # current_app.logger.info("Sign in")
    # return render_template("auth/sign_in.html", form=form)

    if form.validate_on_submit():
        user = UserDB.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', "warning")
            return redirect(url_for('sign_in'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = f"user/{user.username}"
        return redirect(next_page)
    return render_template('auth/sign_in.html', title='Sign In', form=form)


def sign_up():
    if current_user.is_authenticated:
        logger.info("Redirection for sign_up to me")
        return redirect(url_for('me'))
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        UserDB.create_user(
            username=form.username.data,
            email=form.email.data,
            passwd=form.password.data
            # active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("sign_in"))
    else:
        print(f"ERROR {form}")
    return render_template("auth/sign_up.html", form=form)


def log_out():
    logger.info("Logging out")
    logout_user()
    return render_template("about.html")
