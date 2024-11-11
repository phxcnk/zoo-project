import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_ticket_price_child(self):
        self.assertEqual(self.zoo.get_ticket_price(10), 50)

    def test_ticket_price_teen(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_ticket_price_adult(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_ticket_price_senior(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(-1)

if __name__ == '__main__':
    unittest.main()
