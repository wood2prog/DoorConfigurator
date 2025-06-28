import unittest
from src.door import Door
from src.part import Part


class Test_Door(unittest.TestCase):

    def setUp(self):
        self.test_door = Door(123, 10, 20)
        self.test_door.add_part("a", 1, 2, 3)

    def test_should_return_list_of_parts(self):
        self.assertEqual(type(self.test_door.parts), list)

    def test_should_return_first_list_item(self):
        self.assertEqual(type(self.test_door.parts[0]), Part)
