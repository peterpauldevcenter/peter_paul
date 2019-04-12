from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion

# replaced with connexion
# app = Flask(__name__, template_folder='templates')
# app.config.from_object('config')

# connexion reads swagger.yml from the specification_dir below
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def home():
    """
    This function returns a basic homepage

    Returns: the rendered template 'home.html'
    """
    return render_template('home.html')


@app.errorhandler(404)
def not_found(error):
    """
    This function returns a canned 404 message

    Args:
        error:

    Returns: the rendered template '404.html'
    """
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from peter_paul.auth.views import mod_auth as auth_module

# Register blueprint(s)
# app.register_blueprint(auth_module)

db.create_all()
