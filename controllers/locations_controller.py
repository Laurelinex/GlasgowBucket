from flask import Flask, Blueprint, render_template

from models.location import Location

import repositories.location_repository as location_repository

locations_blueprint = Blueprint("locations", __name__)

@locations_blueprint.route("/places")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", locations = locations)

@locations_blueprint.route("/places/<id>", methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    return render_template('locations/show.html', location = location)