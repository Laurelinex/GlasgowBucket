class Location:

    def __init__(self, name, category, description, zone, visited = False, id = None):
        self.name = name
        self.category = category
        self. description = description
        self.zone = zone
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True