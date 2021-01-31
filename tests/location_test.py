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
    
    def test_location_starts_no_picture(self):
        self.assertEqual("", self.location.picture)
    
    def test_location_can_have_picture_url(self):
        self.location.add_picture("https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F9637735a-8f9e-11e9-93de-1ab642214bd5.jpg?crop=2667%2C1500%2C0%2C0&resize=1180")
        self.assertEqual("https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F9637735a-8f9e-11e9-93de-1ab642214bd5.jpg?crop=2667%2C1500%2C0%2C0&resize=1180", self.location.picture)