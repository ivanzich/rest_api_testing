from unittest import TestCase
from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument ")
        self.assertEqual(item.price, 19.99)

    def test_item_json(self):
        item = ItemModel('test', 19.99)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(item.json(), expected,
                         "The JSON export of the item is incorrect. Received {}, expected {}".format(item.json(), expected))
