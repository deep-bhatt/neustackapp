from flask import request, jsonify
from models.models import Item, Cart, Order

def cart_routes(app, cart: Cart):
  @app.route('/cart/add', methods=['POST'])
  def add_to_cart():
    data = request.json
    item = Item(data['id'], data['name'], data['price'])
    cart.items.append(item)

    return jsonify(
      {"message": "Item added to cart"},
      {"cart": cart.to_dict()}
    ), 200

  @app.route('/checkout', methods=['POST'])
  def checkout():
    # checkouts cart & creates an order
    return jsonify({'msg': 'to be implemented'}), 501
