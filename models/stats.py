# An attempt to make attributes avaiable globally
# For achieving 'Singleton'

_discount_codes_generated = []
_item_purchased_count = 0
_total_orders_placed = 0
_total_purchase_amount = 0
_total_discount_amount = 0

# stores user: discountCode key - value pairs
_valid_discount_codes = {}

# Discount code generated every 3rd order.
_nth_order_discount = 3

def get_discount_codes_generated():
  return _discount_codes_generated

def add_generated_discount_code(code):
  _discount_codes_generated.append(code)

def get_item_purchased_count():
  return _item_purchased_count

def increment_item_purchased_count(count):
  global _item_purchased_count
  _item_purchased_count += count

def get_total_orders_placed():
  return _total_orders_placed

def increment_total_orders_placed():
  global _total_orders_placed
  _total_orders_placed += 1

def get_total_purchase_amount():
  return _total_purchase_amount

def add_to_total_purchase_amount(amount):
  global _total_purchase_amount
  _total_purchase_amount += amount

def get_total_discount_amount():
  return _total_discount_amount

def add_to_total_discount_amount(amount):
  global _total_discount_amount
  _total_discount_amount += amount

def get_valid_discount_code(user):
  return _valid_discount_codes.get(user, '')

def set_valid_discount_code(user, code):
  _valid_discount_codes[user] = code

def remove_valid_discount_code(user):
  _valid_discount_codes[user] = ''

def nth_order_discount():
  return _nth_order_discount