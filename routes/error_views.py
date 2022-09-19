from flask import render_template, flash, redirect, url_for


def page_not_found(error):
    return render_template("404.html")


def unauthorized(error):
    flash("Please, log in.", "info")
    return redirect(url_for("sign_in"))
