from app import app
from flask import render_template
from models.book_orders import book_orders

@app.route('/orders')
def index():
    return render_template("index.html", title = "Home", orders = book_orders)

@app.route('/order/<index>')
def get_order(index):
    return render_template("order.html", title = "Order", order = book_orders[int(index)])