from flask import Blueprint
import models.user 

app = Blueprint('users',__name__)

#user page address
@app.route('/user')
def user():
    return 'user page'

