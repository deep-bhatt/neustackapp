import unittest
from unittest.mock import patch
from services.discount import DiscountService

class TestDiscountService(unittest.TestCase):
  @patch('services.discount.get_total_orders_placed')
  @patch('services.discount.nth_order_discount')
  def test_is_discount_applicable(self, mock_nth_order_discount, mock_get_total_orders_placed):
    # Given
    mock_nth_order_discount.return_value = 4
    mock_get_total_orders_placed.return_value = 3

    # When
    result = DiscountService.is_discount_applicable()

    # Then
    self.assertTrue(result)

  def test_generate_discount_code(self):
    """ Discount code should be in upper case having 6 letters. """
    code = DiscountService.generate_discount_code()
    self.assertEqual(len(code), 6)
    self.assertTrue(code.isupper())

  @patch('services.discount.get_valid_discount_code')
  def test_validate_discount_code(self, mock_get_valid_discount_code):
    # Given
    mock_get_valid_discount_code.return_value = 'ABCDEF'

    # When
    valid = DiscountService.validate_discount_code('user1', 'ABCDEF')
    # Then
    self.assertTrue(valid)

    # When
    invalid = DiscountService.validate_discount_code('user1', 'XYZ123')
    # Then
    self.assertFalse(invalid)
