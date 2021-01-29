import pdb
from models.location import Location
from models.zone import Zone

import repositories.location_repository as location_repository
import repositories.zone_repository as zone_repository

location_repository.delete_all()
zone_repository.delete_all()

zone_1 = Zone("City Centre")
zone_repository.save(zone_1)
zone_2 = Zone("North Glasgow")
zone_repository.save(zone_2)
zone_3 = Zone("Southside")
zone_repository.save(zone_3)
zone_4 = Zone("East End")
zone_repository.save(zone_4)
zone_5 = Zone("West")
zone_repository.save(zone_5)

location_1 = Location("Necropolis", "A Victorian garden cemetery", zone_1)
location_repository.save(location_1)

zone_5.name = "West End"
zone_repository.update(zone_5)

location_1.description = "A fascinating Victorian garden cemetery adjacent to Glasgow Cathedral"
location_repository.update(location_1)

pdb.set_trace()