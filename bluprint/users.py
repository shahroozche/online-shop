from flask import Blueprint

app = Blueprint('users',__name__)

#user page address
@app.route('/user')
def user():
    return 'user page'

