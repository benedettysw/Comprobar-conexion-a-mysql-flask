from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


MyWeb = Flask(__name__)


#CONFIGURACION Y CONEXION A LA BASE DE DATO

MyWeb.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/facebook'
MyWeb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Cuando trabajas con sesiones de usuario - Por ejemplo, para mantener un usuario logueado:

MyWeb.secret_key = "planas1"


db = SQLAlchemy(MyWeb)
ma = Marshmallow(MyWeb)


