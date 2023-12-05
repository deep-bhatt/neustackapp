from flask import request, jsonify

def cart_routes(app):

  @app.route('/cart/add', methods=['POST'])
  def add_to_cart():
    # add items to cart
    return jsonify({'msg': 'to be implemented'}), 501

  @app.route('/checkout', methods=['POST'])
  def checkout():
    # checkouts cart & creates an order
    return jsonify({'msg': 'to be implemented'}), 501
