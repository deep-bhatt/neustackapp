import random
import string
from models.stats import *

class DiscountService:
  @staticmethod
  def is_discount_applicable():
    # n is the nth order
    if nth_order_discount() == 1 or nth_order_discount() == 0:
      return True

    if get_total_orders_placed() == 0:
      return False

    return (get_total_orders_placed()+1) % nth_order_discount() == 0

  @staticmethod
  def generate_discount_code(length=6):
    """ Generate a random discount code of specified length. """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))

  @staticmethod
  def validate_discount_code(code) -> bool:
    """ Returns True if discount code is valid. """
    if code and code not in get_valid_discount_codes():
      return False

    return True
