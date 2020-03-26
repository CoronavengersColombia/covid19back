import os
import graphene
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask import Flask


app = Flask(__name__)
app.debug = True
app.config['host'] = '0.0.0.0'

basedir = os.path.abspath(os.path.dirname(__file__))

# Logging
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

# SQLAlchemy
app.config['SECRET_KEY'] = os.environ.get('secret_key') or 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///{}'.format(os.path.join(basedir, 'app.db'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Migrations
migrate = Migrate(app, db)

# Marshamallow
ma = Marshmallow(app)

# Blueprints
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import routes, models
