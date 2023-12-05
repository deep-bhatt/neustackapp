from flask import request, jsonify
from models.models import Item, Order, CartManager, Cart
from services.discount import DiscountService
from store.stats import *

def cart_routes(app, cart_manager: CartManager):
  @app.route('/cart/add', methods=['POST'])
  def add_to_cart():
    data = request.json
    userId = request.headers.get('x-user-id')

    item = Item(data['id'], data['name'], data['price'])
    cart: Cart = cart_manager.get_cart(userId)
    cart.items.append(item)

    # returns discount code if already previously generated for
    # this user.
    code = get_valid_discount_code(userId)

    if not code and DiscountService.is_discount_applicable():
      code = DiscountService.generate_discount_code()
      add_generated_discount_code(code)
      set_valid_discount_code(userId, code)

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
    userId = request.headers.get('x-user-id')
    cart = cart_manager.get_cart(userId)

    if not len(cart.items):
      return jsonify({'error': 'cart is empty'}), 400

    code = ''
    if data and data['discountCode']:
      code = data['discountCode']

    if not DiscountService.validate_discount_code(userId, code):
      return jsonify({'error': 'discount code invalid'}), 400

    # checkouts cart & creates an order
    order = Order()
    order.items = cart.items
    order.total = sum(item.price for item in cart.items)
    order.discount_code = code

    if order.discount_code:
      order.total_discount_availed = 0.1 * order.total
      order.total = order.total - order.total_discount_availed

    # clear discount codes
    reset_valid_discount_codes()

    # Update stats
    add_to_total_discount_amount(order.total_discount_availed)
    add_to_total_purchase_amount(order.total)
    increment_total_orders_placed()
    increment_item_purchased_count(len(order.items))

    # reset cart after checkout
    cart_manager.reset_cart(userId)

    resp = {
      'msg': 'Order placed successfully.',
      'total_orders_placed': get_total_orders_placed()
    }

    return jsonify(resp), 201
