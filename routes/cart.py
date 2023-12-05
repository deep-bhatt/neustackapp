from flask import request, jsonify
from models.models import Item, Order, CartManager, Cart
from services.discount import DiscountService
from models.stats import *

def cart_routes(app, cart_manager: CartManager):
  @app.route('/cart/add', methods=['POST'])
  def add_to_cart():
    data = request.json
    item = Item(data['id'], data['name'], data['price'])
    cart: Cart = cart_manager.get_cart()
    cart.items.append(item)

    code = ''
    if DiscountService.is_discount_applicable():
      code = DiscountService.generate_discount_code()
      add_generated_discount_code(code)
      add_valid_discount_code(code)

    resp = {
      "message": "Item added to cart",
      "cart": cart.to_dict(),
    }

    if code:
      resp['discountCode'] = code

    return jsonify(resp), 200

  @app.route('/checkout', methods=['POST'])
  def checkout():
    data = request.json
    cart = cart_manager.get_cart()

    if not len(cart.items):
      return jsonify({'error': 'cart is empty'}), 400

    code = ''
    if data and data['discountCode']:
      code = data['discountCode']

    if not DiscountService.validate_discount_code(code):
      return jsonify({'error': 'discount code invalid'}), 400

    # checkouts cart & creates an order
    order = Order()
    order.items = cart.items
    order.total = sum(item.price for item in cart.items)
    order.discount_code = code

    if order.discount_code:
      order.total_discount_availed = 0.1 * order.total
      order.total = order.total - order.total_discount_availed
      remove_valid_discount_code(order.discount_code)

    # Update stats
    add_to_total_discount_amount(order.total_discount_availed)
    add_to_total_purchase_amount(order.total)
    increment_total_orders_placed()
    increment_item_purchased_count(len(order.items))

    # reset cart after checkout
    cart_manager.reset_cart()

    resp = {
      'msg': 'Order placed successfully.',
      'total_orders_placed': get_total_orders_placed()
    }

    return jsonify(resp), 201
