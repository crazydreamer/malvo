from flask import render_template, redirect, url_for, flash
from flask.ext.login import login_user

from . import auth
from .forms import RegistrationForm
from ..models import Team, Member
from .. import db


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        db.create_all()
        team = Team.query.filter_by(name=form.name.data).first()
        if team is not None:
            flash('Team name unavailable')
            return redirect(url_for('.register'))
        team = Team(
            name=form.name.data,
            password=form.password.data
        )
        member_one = Member(
            name=form.member_one_name.data,
            phone=form.member_one_phone.data,
            id=form.member_one_phone.data,
            team=team
        )
        if form.member_two_name.data is not None:
            member_two = Member(
                name=form.member_two_name.data,
                phone=form.member_two_phone.data,
                id=form.member_two_phone.data,
                team=team
            )
            db.session.add(member_two)
        db.session.add(member_one)
        db.session.add(team)
        db.session.commit()
        print('Done')
        flash('{} was registered successfully'.format(form.name.data))
        return redirect(url_for('.login'))
    return render_template('auth/register.html', form=form)
