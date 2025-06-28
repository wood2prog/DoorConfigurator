import unittest
from src.part import Part


class Test_Part(unittest.TestCase):

    def setUp(self):
        self.testPart = Part("a", 1, 2, 3)

    def test_part_name(self):
        self.assertEqual(self.testPart.name(), "a")

    def test_part_return_width(self):
        self.assertEqual(self.testPart.width(), 1)

    def test_part_return_length(self):
        self.assertEqual(self.testPart.length(), 2)

    def test_should_return_thickness(self):
        self.assertEqual(self.testPart.thickness(), 3)
