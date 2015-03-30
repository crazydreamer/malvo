from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True, index=True)
    member_one = db.Column(db.String(64), nullable=False)
    member_one_id = db.Column(db.Integer, nullable=False, unique=True, index=True)
    member_one_phone = db.Column(db.Integer, nullable=False)
    member_two = db.Column(db.String(64))
    member_two_id = db.Column(db.Integer, unique=True)
    member_two_phone = db.Column(db.Integer)
    mcq_score = db.Column(db.Integer, default=0)
    prog_score = db.Column(db.Integer, default=0)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_team(user_id):
    return User.query.get(int(user_id))