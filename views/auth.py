import psycopg2
import psycopg2.extras
from flask import Flask, render_template, redirect, url_for, session, flash, request


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

        # conn = config.get_db_connection()
        # cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        # cursor.execute("INSERT INTO users VALUES (%s, %s)", (first_name, last_name, email,))
        flash(f"Ok, you have added", category="success")
        # conn.commit()
        return render_template("auth/sign_in.html")

    return render_template("auth/sign_up.html")


def log_out():
    return render_template("auth/log_out.html")
