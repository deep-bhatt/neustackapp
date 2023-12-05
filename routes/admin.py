from flask import jsonify
from store.stats import *
from models.cart import CartManager

def admin_routes(app, cart_manager: CartManager):

  @app.route('/stats', methods=['GET'])
  def get_statistics():
    resp = {
      'total_orders_placed': get_total_orders_placed(),
      'items_purchased_count': get_item_purchased_count(),
      'total_purchase_amount': get_total_purchase_amount(),
      'discount_codes_generated': get_discount_codes_generated(),
      'total_discount_availed': get_total_discount_amount(),
    }
    return jsonify(resp), 200

  @app.route('/reset', methods=['POST'])
  def reset():
    cart_manager.reset_all_carts()
    reset_stats()
    return jsonify({'msg': 'app reset success'}), 200
