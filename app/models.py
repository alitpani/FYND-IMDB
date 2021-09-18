from flask_login import UserMixin,current_user
from app import db,login,admin
from flask_admin.contrib.sqla import ModelView
from flask import redirect,url_for,make_response,jsonify


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False) 

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    popularity = db.Column(db.String(60))
    director =  db.Column(db.String(60))
    genre = db.Column(db.PickleType())
    imdb_score = db.Column(db.Integer())
    name = db.Column(db.String(20),nullable=False)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_tmp'))

admin.add_view(MyModelView(Movies,db.session))