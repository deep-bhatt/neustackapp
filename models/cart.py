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
