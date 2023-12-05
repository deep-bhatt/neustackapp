from flask import jsonify
from store.stats import *

def admin_routes(app):

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
