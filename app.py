from flask import Flask
from flask_wtf.csrf import CSRFProtect
from bluprint.general import app as general
from bluprint.admin import app as admin
from bluprint.users import app as users
import config
import extensions
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(users)

csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = config.SECRET_KEY
extensions.db.init_app(app)

with app.app_context():
    extensions.db.create_all()

if __name__ == '__main__':
    app.run(debug=True)