from datetime import datetime
from peter_paul.config import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base):

    __tablename__ = 'auth_user'

    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, usersname, email, password):

        self.name = usersname
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.usersname}>'
