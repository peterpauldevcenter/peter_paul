# Define the application directory
import pathlib

# Statement for enabling the development environment
DEBUG = True

PROJECT_ROOT = pathlib.Path(__file__).parent
BASE_DIR = PROJECT_ROOT.absolute()

# Define the database - we are working with
# SQLite for this example
DATABASE_PATH = PROJECT_ROOT / pathlib.Path('app.db')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH.absolute()
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = 'secret'

# Secret key for signing cookies
SECRET_KEY = 'secret'
