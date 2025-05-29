from flask import Flask

from bluprint.general import app as general
from bluprint.admin import app as admin
from bluprint.users import app as users
import config
import extensions

app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(users)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
extensions.db.init_app(app)

with app.app_context():
    extensions.db.create_all()

if __name__ == '__main__':
    app.run()