class Item:
  def __init__(self, id, name, price):
    self.id = id
    self.name = name
    self.price = price

class Cart:
  def __init__(self):
    self.items = []

class Order:
  def __init__(self):
    self.items = []
    self.total = 0
    self.discount_code = None

# Singleton Class
class Stats:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Stats, cls).__new__(cls)
      cls._instance.item_purchased_count = {}
      cls._instance.total_purchase_amount = 0
      cls._instance.discount_codes_generated = []
      cls._instance.total_discount_amount = 0
    return cls._instance
