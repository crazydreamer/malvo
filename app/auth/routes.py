from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user

from . import auth
from .forms import RegisterForm
from ..models import User
from .. import db

@auth.route('/login')
def login():
    return 'Login'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(csrf_enabled=False)
    if form.validate_on_submit():
        db.create_all()
        user = User.query.filter_by(name=form.name.data).first()
        if user is not None:
            flash('Username unavailable')
            return redirect(url_for('.register'))
        user = User(
            name=form.name.data,
            member_one=form.member_one.data,
            member_one_id=form.member_one_id.data,
            member_one_phone=form.member_one_phone.data,
            member_two=form.member_two.data,
            member_two_id=form.member_two_id.data,
            member_two_phone=form.member_two_phone.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('{} was registed successfully'.format(form.name.data))
        return redirect(url_for('.register'))
    return render_template('/auth/register.html', form=form)