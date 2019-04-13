import pathlib


# statements for enabling the development environment
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# statements for setting up relative paths
PACKAGE_PATH = pathlib.Path(__file__).parent
PROJECT_PATH = PACKAGE_PATH.parent
BASE_DIR = PACKAGE_PATH.absolute()

# statements for setting up a development database at the project root (alongside venv/tests/docs/peter_paul)
# these settings should be overridden by the production environmental variables
DATABASE_PATH = PROJECT_PATH / pathlib.Path('peter_paul.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH.absolute()
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# key for signing data
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'secret'

# key for signing cookies
SECRET_KEY = 'secret'
