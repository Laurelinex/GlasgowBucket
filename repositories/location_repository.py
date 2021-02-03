from db.run_sql import run_sql

from models.zone import Zone
from models.location import Location

import repositories.zone_repository as zone_repository
import repositories.category_repository as category_repository

def save(location):
    sql = "INSERT INTO locations (name, address, description, zone_id, category_id, picture, lockdown_friendly, free, visited) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [location.name, location.address, location.description, location.zone.id, location.category.id, location.picture, location.lockdown_friendly, location.free, location.visited]
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
        category = category_repository.select(row['category_id'])
        location = Location(row['name'], row['address'], row['description'], zone, category, row['picture'], row['lockdown_friendly'], row['free'], row['visited'], row['id'])
        locations.append(location)
    return locations

def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        zone = zone_repository.select(result['zone_id'])
        category = category_repository.select(result['category_id'])
        location = Location(result['name'], result['address'], result['description'], zone, category, result['picture'], result['lockdown_friendly'], result['free'], result['visited'], result['id'])
    return location

def update(location):
    sql = "UPDATE locations SET (name, address, description, zone_id, category_id, picture, lockdown_friendly, free, visited) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [location.name, location.address, location.description, location.zone.id, location.category.id, location.picture, location.lockdown_friendly, location.free, location.visited, location.id]
    print(values)
    run_sql(sql, values)

def select_by_zone(zone):
    locations = []
    sql = "SELECT * FROM locations WHERE zone_id = %s"
    values = [zone.id]
    results = run_sql(sql, values)

    for row in results:
        zone = zone_repository.select(row['zone_id'])
        category = category_repository.select(row['category_id'])
        location = Location(row['name'], row['address'], row['description'], zone, category, row['picture'], row['lockdown_friendly'], row['free'], row['visited'], row['id'])
        locations.append(location)
    return locations

def select_by_category(category):
    locations = []
    sql = "SELECT * FROM locations WHERE category_id = %s"
    values = [category.id]
    results = run_sql(sql, values)

    for row in results:
        zone = zone_repository.select(row['zone_id'])
        category = category_repository.select(row['category_id'])
        location = Location(row['name'], row['address'], row['description'], zone, category, row['picture'], row['lockdown_friendly'], row['free'], row['visited'], row['id'])
        locations.append(location)
    return locations

def select_by_visited(visited):
    locations = []
    sql = "SELECT * FROM locations WHERE visited = %s"
    values = [visited]
    results = run_sql(sql, values)

    for row in results:
        zone = zone_repository.select(row['zone_id'])
        category = category_repository.select(row['category_id'])
        location = Location(row['name'], row['address'], row['description'], zone, category, row['picture'], row['lockdown_friendly'], row['free'], row['visited'], row['id'])
        locations.append(location)
    return locations

def select_by_lockdown_friendliness(lockdown_friendly):
    locations = []
    sql = "SELECT * FROM locations WHERE lockdown_friendly = %s"
    values = [lockdown_friendly]
    results = run_sql(sql, values)

    for row in results:
        zone = zone_repository.select(row['zone_id'])
        category = category_repository.select(row['category_id'])
        location = Location(row['name'], row['address'], row['description'], zone, category, row['picture'], row['lockdown_friendly'], row['free'], row['visited'], row['id'])
        locations.append(location)
    return locations

def select_by_free_entry(free):
    locations = []
    sql = "SELECT * FROM locations WHERE free = %s"
    values = [free]
    results = run_sql(sql, values)

    for row in results:
        zone = zone_repository.select(row['zone_id'])
        category = category_repository.select(row['category_id'])
        location = Location(row['name'], row['address'], row['description'], zone, category, row['picture'], row['lockdown_friendly'], row['free'], row['visited'], row['id'])
        locations.append(location)
    return locations

def mark_visited(id):
    sql = "UPDATE locations SET visited = true WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def mark_not_visited(id):
    sql = "UPDATE locations SET visited = false WHERE id = %s"
    values = [id]
    run_sql(sql, values)