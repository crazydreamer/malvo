from flask import render_template, redirect, url_for, flash, request
from flask.ext.login import login_user, logout_user, login_required

from . import auth
from .forms import RegistrationForm
from .forms import LoginForm
from ..models import Team, Member
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        team = Team.query.filter_by(name=form.team_name.data).first()
        if team is None or not team.verify_password(form.password.data):
            flash('Invalid Team Name or Password')
            return redirect(url_for('.login'))
        login_user(team)
        flash('{} logged in successfully'.format(form.team_name.data))
        return redirect(url_for('.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out')
    return redirect(url_for('.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db.create_all()
        team = Team.query.filter_by(name=form.name.data).first()
        if team is not None:
            flash('Team name unavailable')
            return render_template('auth/register.html', form=form)
        team = Team(
            name=form.name.data,
            password=form.password.data
        )
        member_one = Member(
            name=form.member_one_name.data,
            phone=form.member_one_phone.data,
            college_id=form.member_one_id.data,
            team=team
        )
        if form.member_two_name.data:
            member_two = Member(
                name=form.member_two_name.data,
                phone=form.member_two_phone.data,
                college_id=form.member_two_id.data,
                team=team
            )
            db.session.add(member_two)
        db.session.add(member_one)
        db.session.add(team)
        db.session.commit()
        flash('{} was registered successfully'.format(form.name.data))
        return redirect(url_for('.login'))
    if request.method == 'POST':
        flash('Form validation error')
        return render_template('auth/register.html', form=form)
    return render_template('auth/register.html', form=form)
