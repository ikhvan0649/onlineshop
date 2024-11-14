# app/views.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Product, Order
from app.schemas import UserSchema, ProductSchema, OrderSchema

main = Blueprint("main", __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# Routes for User
@main.route("/users", methods=["POST"])
def add_user():
    name = request.json["name"]
    email = request.json["email"]
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@main.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

# Routes for Product
@main.route("/products", methods=["POST"])
def add_product():
    name = request.json["name"]
    price = request.json["price"]
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product)

@main.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

# Routes for Order
@main.route("/orders", methods=["POST"])
def add_order():
    user_id = request.json["user_id"]
    product_id = request.json["product_id"]
    quantity = request.json["quantity"]
    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    db.session.add(new_order)
    db.session.commit()
    return order_schema.jsonify(new_order)

@main.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return orders_schema.jsonify(orders)
