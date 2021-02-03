from db.run_sql import run_sql

from models.zone import Zone
from models.location import Location

def save(zone):
    sql = "INSERT INTO zones (name, description, picture) VALUES (%s, %s, %s) RETURNING *"
    values = [zone.name, zone.description, zone.picture]
    results = run_sql(sql, values)
    id = results[0]['id']
    zone.id = id
    return zone

def delete_all():
    sql = "DELETE FROM zones"
    run_sql(sql)

def select_all():
    zones = []

    sql = "SELECT * FROM zones"
    results = run_sql(sql)

    for row in results:
        zone = Zone(row['name'], row['description'], row['picture'], row['id'])
        zones.append(zone)
    return zones

def select(id):
    zone = None
    sql = "SELECT * FROM zones WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        zone = Zone(result['name'], result['description'], result['picture'], result['id'] )
    return zone

# Note: below functions aren't used in the code but were part of the initial MVP and working.
# I left them out because it wouldn;t make sense for the user to be able to update or remove a specific zone in Glasgow.
# I know the North isn't very popular but still.

def update(zone):
    sql = "UPDATE zones SET name = %s WHERE id = %s"
    values = [zone.name, zone.description, zone.picture, zone.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE ROM zones WHERE id = %s"
    values = [id]
    run_sql(sql, values)