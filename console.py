import pdb
from models.location import Location
from models.zone import Zone
from models.category import Category

import repositories.location_repository as location_repository
import repositories.zone_repository as zone_repository
import repositories.category_repository as category_repository

location_repository.delete_all()
category_repository.delete_all()
zone_repository.delete_all()

zone_1 = Zone("City Centre", "The stunning Victorian architecture and grid system of streets make Glasgow’s bustling city centre a distinctive, culture-rich neighbourhood, with George Square – the city’s principal square – its civic heart.", "https://www.fineholm.co.uk/wp-content/uploads/2016/04/property-for-rent-in-glasgow2.jpg")
zone_repository.save(zone_1)
zone_2 = Zone("North Glasgow", "The city's north has rejuvenated in recent years to become an urban playground, a wonder of wildlife, green space and hub of creativity with a community spirit; and all without forgetting its important industrial heritage based on the canal network.  So what better way to start ticking visits off your bucket list than on its very own water pathway?", "https://peoplemakeglasgow.com/images/Neighbourhoods/North/Speirs_Wharf_995.jpg")
zone_repository.save(zone_2)
zone_3 = Zone("Southside", "Located just south of the River Clyde and close to the city centre, this part of town is densely packed with traditional 19th century tenements and an abundance of things to see and do.", "http://s1homesblog.s1thecompany.com/wp-content/uploads/2018/03/pollok-park.-lowjpg-1024x670.jpg")
zone_repository.save(zone_3)
zone_4 = Zone("East End", "Just a short walk from Glasgow city centre lies the east, the historic heart of the city. Home to the city's oldest buildings and some of the most exciting new developments in Glasgow, this neighbourhood offers an easily accessible blend of creativity and heritage, brought to life by a friendly community spirit.", "https://peoplemakeglasgow.com/images/Neighbourhoods/East/st_mungo_mural.jpg")
zone_repository.save(zone_4)
zone_5 = Zone("West End", "With amazing historic attractions tucked in between leafy surroundings, award-winning food and drink and a friendly character, the west has it all.", "https://blog.laterooms.com/wp-content/uploads/2014/04/Ashton-Lane-daytime.jpg")
zone_repository.save(zone_5)

# Location Categories
category_1 = Category("Food & Drink")
category_repository.save(category_1)
category_2 = Category("Museums")
category_repository.save(category_2)
category_3 = Category("Sights & Landmarks")
category_repository.save(category_3)
category_4 = Category("Nature & Parks")
category_repository.save(category_4)
category_5 = Category("Shopping")
category_repository.save(category_5)
category_6 = Category("Concerts and Shows")
category_repository.save(category_6)
category_7 = Category("Transportation")
category_repository.save(category_7)
category_8 = Category("Monuments & Statues")
category_repository.save(category_8)
category_9 = Category("Other")
category_repository.save(category_9)

# City Centre
location_1 = Location("Duke of Wellington Statue", "This beconed statue has become a symbol of Glasgow's quirky sense of humour.", zone_1, category_8, "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F9637735a-8f9e-11e9-93de-1ab642214bd5.jpg?crop=2667%2C1500%2C0%2C0&resize=1180")
location_repository.save(location_1)
location_2 = Location("The Lighthouse", "Landmark exhibition space dedicated to architecture, design and the city.", zone_1, category_2, "https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzNmYzFkZjE1LTFkMDMtNGQzOC05ODlmLTc3YWIwMDE5MjM5YjkwOGFhNzliMmRhYjM2NzIwOF9MaWdodGhvdXNlX2dsYXNnb3dfc3BpcmFsX3N0YWlyY2FzZS5qcGciXSxbInAiLCJjb252ZXJ0IiwiIl0sWyJwIiwiY29udmVydCIsIi1xdWFsaXR5IDgxIC1hdXRvLW9yaWVudCJdLFsicCIsInRodW1iIiwiNzgweDUyMCMiXV0/Lighthouse_glasgow_spiral_staircase.jpg")
location_repository.save(location_2)

# North Glasgow
location_3 = Location("Speirs Wharf", "Barges and house boats line the canal onto a cobbled street with newly developed canal paths with a network of running and cycle routes.", zone_2, category_3, "https://mr1.homeflow-assets.co.uk/files/photo/image/16509/8339/_x683/GCY190045_16.jpg")
location_repository.save(location_3)

# Southside
location_4 = Location("The Hidden Gardens", "Great wee sanctuary in the southside urban sprawl.", zone_3, category_4, "https://media.timeout.com/images/105374549/630/472/image.jpg")
location_repository.save(location_4)
location_5 = Location("House for an Art Lover", "Combines art gallery and exhibition space, events venue, café, multipurpose artists studios and magnificent visitor attraction into one unique and inspiring venue.", zone_3, category_2, "https://files.list.co.uk/images/2019/10/23/house-for-an-art-lover-1280px-LST375407.jpg")
location_repository.save(location_5)

# East End
location_6 = Location("The People's Palace", "Well-curated museum to dive deeper into how Glaswegians lived before modern day times.", zone_4, category_2, "https://prodglportalv2.azureedge.net/cache/9/9/9/f/d/d/999fdd47ccb23fc992e922f212777f78cece67d0.jpg")
location_repository.save(location_6)
location_7 = Location("Necropolis", "A fascinating Victorian garden cemetery adjacent to Glasgow Cathedral.", zone_4, category_3, "https://www.thescottishsun.co.uk/wp-content/uploads/sites/2/2020/02/NINTCHDBPICT000477166197.jpg?strip=all&w=960")
location_repository.save(location_7)

# West End
location_8 = Location("The Botanic Gardens", "Created in 1817, Glasgow Botanic Gardens feature several glasshouses and incredible plantlife.", zone_5, category_4, "https://cdn.shopify.com/s/files/1/0235/4729/files/1_eabc443d-7f9e-46dc-8fd0-1ff91acc64c1.jpg?v=1499621290")
location_repository.save(location_8)
location_9 = Location("Kelvingrove Art Gallery & Museum", "The most popular attraction in Glasgow. Features vast natural history and art collections.", zone_5, category_2, "https://i.pinimg.com/originals/1a/2e/6b/1a2e6bfa5836a827d8332cedef5d4e99.jpg")
location_repository.save(location_9)

pdb.set_trace()