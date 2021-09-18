from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

app = Flask(__name__)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'


admin = Admin(app) #index_view= MyadminIndexView)


from app import routes