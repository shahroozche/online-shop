from flask import Blueprint,render_template
from models.product import Product


app = Blueprint('general',__name__)

#main page address
@app.route('/')
def main():
    products = Product.query.all()

    return render_template("main.html",products=products)

#about us page address
@app.route('/about')
def about():
    return render_template("about.html")