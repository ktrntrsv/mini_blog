from flask import render_template, redirect, url_for, session, flash, request


def post():
    return render_template("blog/post.html")


def edit_post():
    return render_template("blog/edit_post.html")


def delete_post():
    return render_template("blog/delete_post.html")
