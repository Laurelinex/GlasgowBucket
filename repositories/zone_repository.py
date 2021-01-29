from db.run_sql import run_sql

from models.zone import Zone
from models.location import Location

def save(zone):
    sql = "INSERT INTO zones (name) VALUES (%s) RETURNING *"
    values = [zone.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    zone.id = id
    return zone

def delete_all():
    sql = "DELETE FROM zones"
    run_sql(sql)

def delete(id):
    sql = "DELETE ROM zones WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    zones = []

    sql = "SELECT * FROM zones"
    results = run_sql(sql)

    for row in results:
        zone = Zone(row['name'], row['id'])
        zones.append(zone)
    return zones

def select(id):
    zone = None
    sql = "SELECT * FROM zones WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        zone = Zone(result['name'], result['id'] )
    return zone

def update(zone):
    sql = "UPDATE zones SET name = %s WHERE id = %s"
    values = [zone.name, zone.id]
    run_sql(sql, values)