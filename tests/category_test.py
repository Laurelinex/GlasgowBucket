import unittest

from models.category import Category

class TestCategory(unittest.TestCase):
    
    def setUp(self):
        self.category = Category("Parks")
    
    def test_category_has_name(self):
        self.assertEqual("Parks", self.category.name)