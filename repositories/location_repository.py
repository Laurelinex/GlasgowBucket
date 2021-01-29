from db.run_sql import run_sql

from models.zone import Zone
from models.location import Location

import repositories.zone_repository as zone_repository

def save(location):
    sql = "INSERT INTO locations (name, description, zone_id) VALUES (%s, %s, %s) RETURNING *"
    values = [location.name, location.description, location.zone.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location