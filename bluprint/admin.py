from flask import Blueprint,render_template,request,session,redirect,abort,url_for
import config
from models.product import Product
from extensions import db

app = Blueprint('admin',__name__)


@app.before_request
def before_request():
    if session.get("admin_login",None) == None and request.endpoint != "admin.admin_login":
        abort(403)



#admin login page address
@app.route('/admin/login', methods = ['GET','POST'])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username",None)
        password = request.form.get("password",None)
        if username == config.ADMIN_USERNAME and password == config.ADMIN_PASSWORD :
            session["admin_login"] = username
            return redirect(url_for("admin.admin_dashboard"))
        else:
            return redirect(url_for("admin.admin_login"))
    else:
        return render_template("/admin/login.html")



#admin Dashboard page address
@app.route('/admin/dashboard', methods = ['GET'])
def admin_dashboard():
    return render_template("/admin/dashboard.html")


#admin products ard page address
@app.route('/admin/products', methods = ['GET','POST'])
def products():
    if request.method == "GET":
        products = Product.query.all()
        return render_template("/admin/products.html",products = products )
    else:
        name = request.form.get('name',None)
        description = request.form.get('description',None)
        price = request.form.get('price',None)
        active = request.form.get('active',None)

        p = Product(name = name, description = description , price = price)
        if  active == None:
            p.active = 0
        else:
            p.active = 1
        
        db.session.add(p)
        db.session.commit()

        return "محصول اضافه شد"


#admin edit products ard page address
@app.route('/admin/dashboard/edit-product/<id>', methods = ['GET','POST'])
def edit_products(id):
    product = Product.query.filter(Product.id == id).first_or_404()

    if request.method == "GET":
        
        return render_template("/admin/edit-product.html",product = product )
    
    else:

        name = request.form.get('name',None)
        description = request.form.get('description',None)
        price = request.form.get('price',None)
        active = request.form.get('active',None)

        product.name = name
        product.description = description
        product.price = price
        if  active == None:
            product.active = 0
        else:
            product.active = 1
        
        db.session.commit()

        return redirect(url_for("admin.edit_products", id = id))