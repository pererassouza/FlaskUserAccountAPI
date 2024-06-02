from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    account = db.relationship('Account',
                              backref='user',
                              lazy=True)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_followers = db.Column(db.Integer, nullable=False)
    account_name = db.Column(db.String(15), nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id'),
                        nullable=True)
