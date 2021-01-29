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