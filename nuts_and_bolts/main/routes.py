from flask import Blueprint, render_template
from nuts_and_bolts import db
from nuts_and_bolts.models import Products
from nuts_and_bolts.shared.utils import get_cart

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@main.route('/product_list')
def product_list():
    products = db.session.query(Products).order_by(Products.sku)
    return render_template('product_list.html', products=products)


@main.route('/faq')
def faq():
    return render_template('faq.html')

@main.route('/show_cart')
def show_cart():
    simple_cart = get_cart()
    cart = {}
    products = db.session.query(Products).order_by(Products.id)
    for item in simple_cart:
        for product in products:
            if item == product.id:
                cart[item] = {"name" : product.name,
                "price" : product.price,
                "sku" : product.sku,
                "quantity" : simple_cart[item]}

    return render_template('show_cart.html', cart=cart)
  