from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion


# configure the connexion app
connexion_app = connexion.App(__name__, specification_dir='swagger/')
connexion_app.add_api('student.yml')

# configure the flask app
flask_app = connexion_app.app
flask_app.config.from_pyfile('settings.py', silent=True)
flask_app.config.from_envvar('PETER_PAUL_SETTINGS', silent=True)

# configure sqlalchemy
db = SQLAlchemy(flask_app)

# configure marshmallow
ma = Marshmallow(flask_app)

# Import a module / component using its blueprint handler variable (mod_auth)
from peter_paul.auth.views import mod_auth as auth_module

# Register blueprint(s)
# app.register_blueprint(auth_module)
