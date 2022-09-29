from flask_login import current_user, login_required
from flask import redirect, url_for, render_template, flash, request
from forms.edit_bio_form import EditBioForm
from extentions import logger, db
from models.post_model import Post
from models.user_model import User


@login_required
def me():
    return redirect(url_for('user_page', username=current_user.username))


@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_time.desc())
    return render_template("user/me.html", user=user, posts=posts)


@login_required
def edit_bio(username):
    user = User.query.filter_by(username=username).first_or_404()
    if not user.id == current_user.id:
        flash("Permission denied", "warning")
        return redirect(url_for("user_page", username=username))
    form = EditBioForm(request.form)
    user = current_user
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.commit()
        return redirect(url_for("me"))
    return render_template("user/edit_bio.html", form=form, start_bio=user.bio)


@login_required
def friends():
    users = User.query.order_by(User.username.desc())
    return render_template("user/friends.html", users=users)

@login_required
def delete_user():
    user = current_user
    db.session.delete(user)
    db.session.commit()
    return url_for("sign_in")
