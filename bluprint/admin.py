from flask import Blueprint

app = Blueprint('admin',__name__)

#admin page address
@app.route('/admin')
def admin():
    return 'admin page'

