from flask import Flask
from bluprint.general import app as general
from bluprint.admin import app as admin
from bluprint.users import app as users
app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(admin)
app.register_blueprint(users)



if __name__ == '__main__':
    app.run()