from flask import render_template, redirect, url_for, session, flash, request
from flask_login import current_user, login_required


@login_required
def news():
    return render_template("user/news.html")


def post():
    return render_template("blog/post.html")


def edit_post():
    return render_template("blog/edit_post.html")


def delete_post():
    return render_template("blog/delete_post.html")
