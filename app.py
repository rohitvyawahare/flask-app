from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    surname = db.Column(db.String())

@app.route('/test')
def test():
    return 'Hello World! I am Rohit!'

@app.route('/test_db')
def test_db():
    db.create_all()
    db.session.commit()
    user = User.query.first()
    if not user:
        u = User(name='Rohit', surname='Vyawahare')
        db.session.add(u)
        db.session.commit()
    user = User.query.first()
    return "User '{} {}' is from database".format(user.name, user.surname)

