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
zone_5 = Zone("West End")
zone_repository.save(zone_5)

# City Centre
location_1 = Location("Duke of Wellington Statue", "This beconed statue has become a symbol of Glasgow's quirky sense of humour.", zone_1, "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F9637735a-8f9e-11e9-93de-1ab642214bd5.jpg?crop=2667%2C1500%2C0%2C0&resize=1180", True)
location_repository.save(location_1)
location_2 = Location("The Lighthouse", "Landmark exhibition space dedicated to architecture, design and the city.", zone_1)
location_repository.save(location_2)

# North Glasgow
location_3 = Location("Speirs Wharf", "Barges and house boats line the canal onto a cobbled street with newly developed canal paths with a network of running and cycle routes.", zone_2)
location_repository.save(location_3)

# Southside
location_4 = Location("The Hidden Gardens", "Great wee sanctuary in the southside urban sprawl.", zone_3)
location_repository.save(location_4)
location_5 = Location("House for an Art Lover", "Combines art gallery and exhibition space, events venue, café, multipurpose artists studios and magnificent visitor attraction into one unique and inspiring venue.", zone_3)
location_repository.save(location_5)

# East End
location_6 = Location("The People's Palace", "Well-curated museum to dive deeper into how Glaswegians lived before modern day times.", zone_4)
location_repository.save(location_6)
location_7 = Location("Necropolis", "A fascinating Victorian garden cemetery adjacent to Glasgow Cathedral.", zone_4)
location_repository.save(location_7)

# West End
location_8 = Location("The Botanic Gardens", "Created in 1817, Glasgow Botanic Gardens feature several glasshouses and incredible plantlife.", zone_5)
location_repository.save(location_8)
location_9 = Location("Kelvingrove Art Gallery & Museum", "The most popular attraction in Glasgow. Features vast natural history and art collections.", zone_5)
location_repository.save(location_9)

pdb.set_trace()