class Location:

    def __init__(self, name, address, description, zone, category, picture = "", lockdown_friendly = False, free = False, visited = False, id = None):
        self.name = name
        self.address = address
        self.description = description
        self.zone = zone
        self.category = category
        self.picture = picture
        self.lockdown_friendly = lockdown_friendly
        self.free = free
        self.visited = visited
        self.id = id
