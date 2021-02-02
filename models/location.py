class Location:

    def __init__(self, name, description, zone, category, picture = "", visited = False, id = None):
        self.name = name
        self.description = description
        self.zone = zone
        self.category = category
        self.picture = picture
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True

    def add_picture(self, picture_url):
        self.picture = picture_url