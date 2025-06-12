from flask import Blueprint,render_template
from models.product import Product


app = Blueprint('general',__name__)

#main page address
@app.route('/')
def main():
    products = Product.query.filter(Product.active == 1).all()

    return render_template("main.html",products=products)


#main product page address
@app.route('/products/<id>/<name>')
def product(id,name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    return render_template("product.html", product = product )

#about us page address
@app.route('/about')
def about():
    return render_template("about.html")