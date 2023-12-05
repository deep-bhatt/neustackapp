import unittest
from unittest.mock import patch
from models.cart import Cart, CartManager
from models.item import Item

class TestCart(unittest.TestCase):
  def test_to_dict_empty_cart(self):
    # Given
    cart = Cart()

    # Then
    self.assertEqual(cart.to_dict(), [])

  def test_to_dict_with_items(self):
    # Given
    test_item = Item(1, 'apple', 150)

    cart = Cart()
    cart.items.append(test_item)

    # When
    resp = cart.to_dict()

    # Then
    self.assertEqual(resp, [{
      'id': 1,
      'name': 'apple',
      'price': 150
    }])

class TestCartManager(unittest.TestCase):
  def test_get_cart_new_user(self):
    # Given
    manager = CartManager()
    user_cart: Cart = manager.get_cart("user1")
    test_item = Item(5, 'test123', 120)
    user_cart.items.append(test_item)

    expectedItems = [{
      'id': 5,
      'name': 'test123',
      'price': 120
    }]

    # When
    resp = user_cart.to_dict()

    # Then
    self.assertIsInstance(user_cart, Cart)
    self.assertEqual(resp, expectedItems)

  def test_reset_cart(self):
    # Given
    manager = CartManager()
    manager.get_cart("user1").items.append(Item(0, 'test', 100))

    # When
    manager.reset_cart("user1")
    user_cart = manager.get_cart("user1")

    # Then
    self.assertEqual(user_cart.items, [])

  def test_reset_all_carts(self):
    # Given
    manager = CartManager()
    manager.get_cart("user1")
    manager.get_cart("user2")

    # When
    manager.reset_all_carts()

    # Then
    self.assertEqual(manager.cart, {})
