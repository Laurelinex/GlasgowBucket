import pdb
from models.location import Location
from models.zone import Zone

import repositories.location_repository as location_repository
import repositories.zone_repository as zone_repository

zone_1 = Zone("City Centre")
zone_repository.save(zone_1)

location_1 = Location("Necropolis", "A Victorian garden cemetery", zone_1)
location_repository.save(location_1)

pdb.set_trace()