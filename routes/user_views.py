from flask_login import current_user, login_required
from flask import redirect, url_for, render_template, flash, request
from forms.edit_bio_form import EditBioForm
from extentions import logger, db
from forms.post_form import CreatePostForm
from models.post_model import Post
from models.user_model import User


@login_required
def me():
    return redirect(url_for('user_page', username=current_user.username))


@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first_or_404()
    # posts = user.posts.order_by(Post.publish_time.desc())
    form = CreatePostForm(request.form)
    user = current_user
    if form.validate_on_submit():
        Post.create_post(
            author_id=user.id,
            body=form.post.data
        )
        flash("Post created.", "success")
        return redirect(url_for("me"))
    posts = user.posts.order_by(Post.publish_time.desc())
    return render_template("user/user.html", user=user, posts=posts, form=form)


@login_required
def edit_bio(username):
    user = User.query.filter_by(username=username).first_or_404()
    if not user.id == current_user.id:
        flash("Permission denied", "warning")
        return redirect(url_for("user_page", username=username))
    form = EditBioForm(request.form)
    user = current_user
    if form.validate_on_submit():
        user.update_bio(form.bio.data)
        return redirect(url_for("me"))
    return render_template("user/edit_bio.html", form=form, start_bio=user.bio)


# @login_required
def friends():
    users = User.query.order_by(User.username.desc())
    return render_template("user/friends.html", users=users)


@login_required
def delete_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if not user == current_user:
        flash("Permission denied", "warning")
        return url_for("me")
    user.delete()
    return url_for("sign_in")
