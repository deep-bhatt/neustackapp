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

class CartManager:
  def __init__(self):
    self.cart = {}

  def get_cart(self, user: str):
    self.cart[user] = self.cart.get(user, Cart())
    return self.cart[user]

  def reset_cart(self, user: str):
    if user in self.cart:
      self.cart[user] = Cart()

    return self.cart[user]

  def reset_all_carts(self):
    self.cart.clear()

class Order:
  def __init__(self):
    self.items = []
    self.total = 0
    self.discount_code = None
    self.total_discount_availed = 0
