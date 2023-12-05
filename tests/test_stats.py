import unittest
from store import stats

class TestStats(unittest.TestCase):
  def tearDown(self):
    # this will reset stats after each test is run.
    stats.reset_stats()

  def test_increment_total_orders_placed(self):
    self.assertEqual(stats.get_total_orders_placed(), 0)
    stats.increment_total_orders_placed()
    self.assertEqual(stats.get_total_orders_placed(), 1)

  def test_increment_item_purchased_count(self):
    self.assertEqual(stats.get_item_purchased_count(), 0)
    stats.increment_item_purchased_count(5)
    self.assertEqual(stats.get_item_purchased_count(), 5)

  def test_add_to_total_purchase_amount(self):
    self.assertEqual(stats.get_total_purchase_amount(), 0)
    stats.add_to_total_purchase_amount(100)
    self.assertEqual(stats.get_total_purchase_amount(), 100)

  def test_set_and_get_valid_discount_code(self):
    self.assertEqual(stats.get_valid_discount_code('user1'), '')
    stats.set_valid_discount_code('user1', 'ABCDEF')
    self.assertEqual(stats.get_valid_discount_code('user1'), 'ABCDEF')

  def test_set_and_get_generated_discount_code(self):
    self.assertEqual(stats.get_discount_codes_generated(), [])
    stats.add_generated_discount_code('XYZPQR')
    self.assertEqual(stats.get_discount_codes_generated(), ['XYZPQR'])

  def test_set_and_get_total_discount_amount(self):
    self.assertEqual(stats.get_total_discount_amount(), 0)
    stats.add_to_total_discount_amount(500)
    self.assertEqual(stats.get_total_discount_amount(), 500)

  def test_reset_discount_coupons(self):
    stats.set_valid_discount_code('user1', 'TEST12')
    self.assertEqual(stats.get_valid_discount_code('user1'), 'TEST12')

    stats.reset_valid_discount_codes()
    self.assertEqual(stats.get_valid_discount_code('user1'), '')
