from db.run_sql import run_sql

from models.zone import Zone
from models.location import Location

import repositories.zone_repository as zone_repository

def save(location):
    sql = "INSERT INTO locations (name, description, picture, zone_id, visited) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [location.name, location.description, location.picture, location.zone.id, location.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location

def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        zone = zone_repository.select(row['zone_id'])
        location = Location(row['name'], row['description'], zone, row['visited'], row['id'])
        locations.append(location)
    return locations

def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        zone = zone_repository.select(result['zone_id'])
        location = Location(result['name'], result['description'], zone, result['visited'], result['id'])
    return location

def update(location):
    sql = "UPDATE locations SET (name, description, zone_id, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [location.name, location.description, location.zone.id, location.visited, location.id]
    print(values)
    run_sql(sql, values)