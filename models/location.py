class Location:

    def __init__(self, name, description, zone, visited = False, id = None):
        self.name = name
        self. description = description
        self.zone = zone
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True