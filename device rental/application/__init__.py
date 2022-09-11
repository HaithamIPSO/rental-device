from flask import Flask,Blueprint,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 
from flask_login import LoginManager
from flask_login import login_user, current_user, logout_user, login_required
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma= Marshmallow(app)

# app.config['SECRET_KEY'] =  os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')


app.config['SECRET_KEY'] =  "asdja9sd89asdnn8"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/device_rental"


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.Login'
from application.Auth.routes import auth
app.register_blueprint(auth)
from application.Main.routes import main
app.register_blueprint(main)

from application.Admin.routes import admin
app.register_blueprint(admin)