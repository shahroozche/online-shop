from flask import Blueprint

app = Blueprint('general',__name__)

#main page address
@app.route('/')
def helloworld():
    return 'main-page'