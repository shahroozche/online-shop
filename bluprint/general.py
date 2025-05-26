from flask import Blueprint

app = Blueprint('general',__name__)

#main page address
@app.route('/')
def main():
    return 'main-page'

#about us page address
@app.route('/about')
def about():
    return 'about us'