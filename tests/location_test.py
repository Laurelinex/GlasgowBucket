import unittest
from models.location import Location

class TestLocation(unittest.TestCase):
    
    def setUp(self):
        self.location = Location("Necropolis", "Victorian garden cemetery", "City Centre")
    
    def test_location_has_name(self):
        self.assertEqual("Necropolis", self.location.name)

    def test_location_has_description(self):
        self.assertEqual("Victorian garden cemetery", self.location.description)
    
    def test_location_has_zone(self):
        self.assertEqual("City Centre", self.location.zone)
    
    def test_location_visited_starts_false(self):
        self.assertEqual(False, self.location.visited)

    def test_location_can_mark_location_visited(self):
        self.location.mark_visited()
        self.assertEqual(True, self.location.visited)