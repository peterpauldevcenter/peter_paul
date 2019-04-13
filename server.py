import os
from peter_paul.config import flask_app, db
from peter_paul.settings import DATABASE_PATH

if not os.path.exists(DATABASE_PATH.absolute()):
    db.create_all()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8080, debug=True)
