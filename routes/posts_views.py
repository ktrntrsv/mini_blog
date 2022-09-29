from flask import render_template, redirect, url_for, session, flash, request
from flask_login import current_user, login_required
from models.post_model import Post
from forms.post_form import CreatePostForm
from models.user_model import User


@login_required
def news():
    posts = Post.query.order_by(Post.publish_time.desc())
    return render_template("user/news.html", posts=posts)


@login_required
def create_post(username):
    user = User.query.filter_by(username=username).first_or_404()
    if not user.id == current_user.id:
        flash("Permission denied", "warning")
        return redirect(url_for("user_page", username=username))
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
    return render_template("user/me.html", user=user, create_post_form=True, form=form, posts=posts)


@login_required
def edit_post(username):
    return render_template("blog/edit_post.html")


@login_required
def delete_post(username):

    return render_template("blog/delete_post.html")
