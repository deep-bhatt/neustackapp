class Item:
  def __init__(self, id, name, price):
    self.id = id
    self.name = name
    self.price = price

  def to_dict(self):
    """ Convert the object to a dictionary """
    return {
        "id": self.id,
        "name": self.name,
        "price": self.price
    }

class Cart:
  def __init__(self):
    self.items = []

  def to_dict(self):
    """ Convert the object to a dictionary """
    cart = []
    for item in self.items:
      cart.append(item.to_dict())
    return cart

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
