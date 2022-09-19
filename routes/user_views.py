from flask_login import current_user, login_required
from flask import redirect, url_for, render_template, flash, request
from forms.edit_bio_form import EditBioForm
from extentions import logger, db


@login_required
def me():
    return redirect(f"/user/{current_user.username}")


@login_required
def me_user(username):
    return render_template("user/me.html", user=current_user)


@login_required
def edit_bio():
    form = EditBioForm(request.form)
    user = current_user
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.commit()
        return redirect(url_for("me"))
    return render_template("user/edit_bio.html", form=form, start_bio=user.bio)

@login_required
def delete_user():
    pass