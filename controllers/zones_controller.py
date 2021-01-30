from flask import Flask, Blueprint, render_template

from models.zone import Zone

import repositories.zone_repository as zone_repository

zones_blueprint = Blueprint("zones", __name__)

# Zones index page
@zones_blueprint.route("/zones")
def zones():
    zones = zone_repository.select_all()
    return render_template("zones/index.html", all_zones = zones)

# Show specific zone
@zones_blueprint.route("/zones/<id>", methods=['GET'])
def show_zone(id):
    zone = zone_repository.select(id)
    return render_template('zones/show.html', zone = zone)