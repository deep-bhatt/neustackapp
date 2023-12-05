from flask import request, jsonify
from models.models import Item, Cart, Order
from services.discount import DiscountService
from models.stats import discount_codes_generated, valid_discount_codes

def cart_routes(app, cart: Cart):
  @app.route('/cart/add', methods=['POST'])
  def add_to_cart():
    data = request.json
    item = Item(data['id'], data['name'], data['price'])
    cart.items.append(item)

    code = ''
    if DiscountService.is_discount_applicable():
      code = DiscountService.generate_discount_code()
      discount_codes_generated.append(code)
      valid_discount_codes.append(code)

    resp = {
      "message": "Item added to cart",
      "cart": cart.to_dict(),
    }

    if code:
      resp['discountCode'] = code

    return jsonify(resp), 200

  @app.route('/checkout', methods=['POST'])
  def checkout():
    # checkouts cart & creates an order

    # check if discount valid code exist
    # if invalid, throw invalid code error
    # if valid, apply 10% discount on total order price
    # then remove discount code from the valid discount code list

    return jsonify({'msg': 'to be implemented'}), 501
