from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from . import db, login_manager


class Team(UserMixin, db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    members = db.relationship('Member', backref='team', lazy='dynamic')
    mcq_score = db.Column(db.Integer, default=-1, index=True)
    prog_score = db.Column(db.Integer, default=-1, index=True)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return Team.query.get(int(user_id))


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    college_id = db.Column(db.String(64))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
