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

# The Five Glasgow main Areas
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
category_6 = Category("Entertainment")
category_repository.save(category_6)
category_7 = Category("Transportation")
category_repository.save(category_7)
category_8 = Category("Monuments & Statues")
category_repository.save(category_8)
category_9 = Category("Other")
category_repository.save(category_9)

# LF, FREE, VISITED (T/F)

# City Centre
location_1 = Location("Duke of Wellington Statue", "16 Royal Exchange Square, G1 3AG", "This beconed statue has become a symbol of Glasgow's quirky sense of humour. Glasgow City Council found out the hard way; touch the cone at your peril.", zone_1, category_8, "https://www.thetimes.co.uk/imageserver/image/%2Fmethode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F9637735a-8f9e-11e9-93de-1ab642214bd5.jpg?crop=2667%2C1500%2C0%2C0&resize=1180", True, True, True)
location_repository.save(location_1)
location_2 = Location("The Lighthouse", "11 Mitchell Ln, G1 3NU", "Landmark exhibition space dedicated to architecture, design and the city. Formerly housing The Glasgow Herald, The Lighthouse was the first public commission completed by Charles Rennie Mackintosh.", zone_1, category_2, "https://assets.atlasobscura.com/media/W1siZiIsInVwbG9hZHMvcGxhY2VfaW1hZ2VzLzNmYzFkZjE1LTFkMDMtNGQzOC05ODlmLTc3YWIwMDE5MjM5YjkwOGFhNzliMmRhYjM2NzIwOF9MaWdodGhvdXNlX2dsYXNnb3dfc3BpcmFsX3N0YWlyY2FzZS5qcGciXSxbInAiLCJjb252ZXJ0IiwiIl0sWyJwIiwiY29udmVydCIsIi1xdWFsaXR5IDgxIC1hdXRvLW9yaWVudCJdLFsicCIsInRodW1iIiwiNzgweDUyMCMiXV0/Lighthouse_glasgow_spiral_staircase.jpg", False, True)
location_repository.save(location_2)
location_10 = Location("Rogano", "11 Exchange Pl, G1 3AN", "If there’s one Glasgow restaurant to check off the foodie bucket list, this is it. Those iconic art deco doors opened in 1935, and Rogano is still serving up the best in Scottish seafood.", zone_1, category_1, "https://foodanddrink.scotsman.com/wp-content/uploads/2015/04/Rogano2-750x400.jpg", False, False)
location_repository.save(location_10)
location_14 = Location("The Old Hairdressers", "Renfield Ln, G2 5AR", "This independent arts venue is hidden away in the city centre and gives local artists a place to showcase their work.", zone_1, category_1, "http://static.designmynight.com/uploads/2014/01/IMG_5454.jpg", False, False)
location_repository.save(location_14)
location_16 = Location("Blythswood Square Spa", "11 Blythswood Square, G2 4AD", "City life dragging you down? If relaxation is in order then you can’t do much better than Blythswood Square, a five star spa hotel in the heart of the city - a hot stone massage and mud wrap await.", zone_1, category_9, "https://i2-prod.glasgowlive.co.uk/incoming/article11102014.ece/ALTERNATES/s615b/Blythswood-Square.jpg", False, False)
location_repository.save(location_16)
location_18 = Location("Central Station", "Gordon St, G1 3SL", "Subterranean passageways beneath Glasgow’s streets. Visit railway vaults that drove Glasgow’s industrial expansion to become ‘The Second City of The British Empire’, hear tales of the famous and infamous who have travelled the tracks and stood on the platforms of Glasgow Central Station.", zone_1, category_3, "https://www.glasgowcentraltours.co.uk/images/portfolio/grid/tour6.jpg", True, True)
location_repository.save(location_18)
location_19 = Location("Glasgow Film Theatre", "12 Rose St, G3 6RB", "Dubbed the first art house cinema to open outside of London (in 1939), the Glasgow Film Theatre (then the Cosmo) has a reputation to uphold. And uphold it does, with the best selection of foreign language and small release films of any Glasgow cinema - not to mention surroundings which are easy on the eye.", zone_1, category_6, "https://files.list.co.uk/images/g/gft-lights-credit-david-grinly-lst090025.jpg", False, False)
location_repository.save(location_19)
location_20 = Location("The Garage", "490 Sauchiehall St, G2 3LW", "A student rite of passage, this Sauchiehall St club holds fond memories for many a Glaswegian. Part of that is queuing up under the big yellow truck - so don't complain about your feet hurting too much. Enjoy the moment - it'll be tinged with nostalgia one day.", zone_1, category_6, "https://i.pinimg.com/originals/e5/69/e8/e569e8f53e8766e7b07a4a4d22185ccb.jpg", False, False)
location_repository.save(location_20)
location_25 = Location("Glasgow Subway", "G1 2LL", "Grab an all-day ticket and tackle all 14 stops.", zone_1, category_7, "https://media-cdn.tripadvisor.com/media/photo-o/0e/2e/3d/99/historic-livery.jpg", True, False)
location_repository.save(location_25)

# North Glasgow
location_3 = Location("Speirs Wharf", "G4 1", "Barges and house boats line the canal onto a cobbled street with newly developed canal paths with a network of running and cycle routes.", zone_2, category_3, "https://mr1.homeflow-assets.co.uk/files/photo/image/16509/8339/_x683/GCY190045_16.jpg", True, True)
location_repository.save(location_3)
location_21 = Location("Maryhill Burgh Halls", "24 Gairbraid Ave, G20 8YE", "This municipal building and public halls first opened in 1878 and was designed by a local architect, Duncan McNaughtan, to resemble a French hotel of that time - a popular style in the 1870s.", zone_2, category_2, "https://images.squarespace-cdn.com/content/v1/4ff41e65e4b03ec22b1153c6/1556030142962-9BFKND11NZB13XARE07R/ke17ZwdGBToddI8pDm48kIn_KhDm18P3HghCBZxCDzl7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1USJ8nKsY77xzqZiG78zydUlC4D_gi5nP0_sA9TvJNHmDx6IdPzJJcGB8slK3sT2FBg/Maryhill+Burgh+Hall+2.jpg?format=1500w", False, True)
location_repository.save(location_21)
location_22 = Location("Mackintosh Queen's Cross", "870 Garscube Rd, G20 7EL", "One of Glasgow's hidden architectural gems. The only church in the world designed by the great Scottish architect, designer and artist, Charles Rennie Mackintosh.", zone_2, category_3, "https://i.pinimg.com/originals/de/78/19/de78190dddf7c13d3ee6554593894da0.jpg", True, True)
location_repository.save(location_22)

# Southside
location_4 = Location("The Hidden Gardens", "25A Albert Dr, G41 2PE", "Great wee sanctuary in the southside urban sprawl.", zone_3, category_4, "https://media.timeout.com/images/105374549/630/472/image.jpg", True, True)
location_repository.save(location_4)
location_5 = Location("House for an Art Lover", "10 Dumbreck Rd, G41 5BW", "Combines art gallery and exhibition space, events venue, café, multipurpose artists studios and magnificent visitor attraction into one unique and inspiring venue.", zone_3, category_2, "https://files.list.co.uk/images/2019/10/23/house-for-an-art-lover-1280px-LST375407.jpg", False, False)
location_repository.save(location_5)
location_23 = Location("Pollok Country Park", "2060 Pollokshaws Rd, G43 1AT", "As Glasgow’s largest park, there’s so much to explore here that you might want to set a few hours aside just to explore this beautiful green space.", zone_3, category_4, "https://peoplemakeglasgow.com/images/Neighbourhoods/South/pollok-park.jpg", True, True)
location_repository.save(location_23)
location_24 = Location("Pollok House", "2060 Pollokshaws Rd, G43 1AT", "The house contains an impressive collection of Spanish paintings, many of which were acquired by the Maxwell family, and the meticulous restoration of the property will let you experience what life was like inside this grand home in the 18th century.", zone_3, category_2, "https://www.visitscotland.com/wsimgs/Pollok-1_1720863373.jpg", False, False)
location_repository.save(location_24)

# East End
location_6 = Location("The People's Palace", "Greens, Templeton St, G40 1AT", "Well-curated museum to dive deeper into how Glaswegians lived before modern day times.", zone_4, category_2, "https://prodglportalv2.azureedge.net/cache/9/9/9/f/d/d/999fdd47ccb23fc992e922f212777f78cece67d0.jpg", False, True)
location_repository.save(location_6)
location_7 = Location("The Necropolis", "Castle St, G4 0UZ", "A fascinating Victorian garden cemetery adjacent to Glasgow Cathedral.", zone_4, category_3, "https://www.thescottishsun.co.uk/wp-content/uploads/sites/2/2020/02/NINTCHDBPICT000477166197.jpg?strip=all&w=960", True, True)
location_repository.save(location_7)
location_15 = Location("Tibo Bistro", "443 Duke St, G31 1RY", "This licenced café is a popular spot for breakfast, lunch and dinner in the east of the city. Its bohemian decor, good music and friendly staff make for a warm and inviting atmosphere.", zone_4, category_1, "https://i2-prod.glasgowlive.co.uk/incoming/article11025255.ece/ALTERNATES/s615b/Cafe-Tibo.jpg", False, False)
location_repository.save(location_15)

# West End
location_8 = Location("The Botanic Gardens", "730 Great Western Rd, G12 0UE", "Created in 1817, Glasgow Botanic Gardens feature several glasshouses and incredible plantlife.", zone_5, category_4, "https://cdn.shopify.com/s/files/1/0235/4729/files/1_eabc443d-7f9e-46dc-8fd0-1ff91acc64c1.jpg?v=1499621290", True, True)
location_repository.save(location_8)
location_9 = Location("Kelvingrove Art Gallery & Museum", "Argyle St, G3 8AG", "The most popular attraction in Glasgow. Features vast natural history and art collections.", zone_5, category_2, "https://i.pinimg.com/originals/1a/2e/6b/1a2e6bfa5836a827d8332cedef5d4e99.jpg", False, True)
location_repository.save(location_9)
location_11 = Location("The Grosvenor Cinema", "24 Ashton Ln, Hillhead, G12 8SJ", "Leave behind the sticky floors of the multiplex for a more refined affair at the Grosvenor. We’re talking leather armchairs - even couches, if you’re feeling flush - and the licence to take a pint in along with your popcorn.", zone_5, category_6, "https://grosvenorwestend.co.uk/wp-content/uploads/screens.jpg", False, False)
location_repository.save(location_11)
location_12 = Location("Voltaire & Rousseau", "12 Otago Ln, G12 8PB", "Without a doubt Glasgow’s most unique bookshop, it is packed floor to ceiling with secondhand texts covering all genres and tastes.", zone_5, category_5, "https://i2-prod.glasgowlive.co.uk/incoming/article11024692.ece/ALTERNATES/s810/Voltaire-and-Rousseau.jpg", False, False)
location_repository.save(location_12)
location_13 = Location("Mixed Up Records", "18 Otago Ln, G12 8PB", "With new releases, rare editions, and some secondhand bargains, a shopping trip for vinyl wouldn’t be complete without visiting Mixed Up Records in Otago Lane.", zone_5, category_5, "https://i2-prod.glasgowlive.co.uk/incoming/article11024829.ece/ALTERNATES/s615b/mixed-up-records.jpg", False, False)
location_repository.save(location_13)
location_17 = Location("The Western Baths", "12 Cranworth St, G12 8BZ", "With a stunning Victorian pool dating back to 1876 in the city, everyone should aim to take a dip in splendid surroundings at least once.", zone_5, category_9, "https://images.squarespace-cdn.com/content/v1/5b4746755cfd79f19b5f423a/1559853669959-L9T78X49NDEE2B54KU73/ke17ZwdGBToddI8pDm48kLmUbQbtDGsZ8YTTasGILul7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0lqfkVpRp1g_2L-WsTQRP4LE6B0BTbA_B4hx17Wb5wfjT9mR3gzq1SMR4UIbU98M4g/DSC_5552.jpg?format=2500w", False, False)
location_repository.save(location_17)

pdb.set_trace()