from flask import Flask, Blueprint, render_template, redirect, request

from models.location import Location

import repositories.location_repository as location_repository
import repositories.zone_repository as zone_repository

locations_blueprint = Blueprint("locations", __name__)

# Locations index page
@locations_blueprint.route("/places")
def locations():
    locations = location_repository.select_all()
    return render_template('locations/index.html', all_locations = locations)

# Show a specific place
@locations_blueprint.route("/places/<id>", methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    return render_template('locations/show.html', location = location)

# Add new place page
@locations_blueprint.route("/places/new")
def new_location():
    zones = zone_repository.select_all()
    locations = location_repository.select_all()
    return render_template('locations/new.html', all_zones = zones, all_locations = locations)

# Create new place
@locations_blueprint.route("/places", methods=['POST'])
def create_location():
    name = request.form['name']
    description = request.form['description']
    zone_id = request.form['zone_id']
    picture = request.form['picture']
    visited = request.form['visited']
    zone = zone_repository.select(zone_id)
    location = Location(name, description, zone, picture, visited)
    location_repository.save(location)
    return redirect('/places')

# Edit place page
@locations_blueprint.route("/places/<id>/edit", methods=['GET'])
def edit_location(id):
    location = location_repository.select(id)
    zones = zone_repository.select_all()
    return render_template('locations/edit.html', location = location, all_zones = zones)

# Update place info
@locations_blueprint.route("/places/<id>", methods=['POST'])
def update_location(id):
    name = request.form['name']
    description = request.form['description']
    zone = request.form['zone_id']
    picture = request.form['picture']
    visited = request.form['visited']
    zone = zone_repository.select(request.form['zone_id'])
    location = Location(name, description, zone, picture, visited, id)
    location_repository.update(location)
    return redirect('/places')

# Delete place
@locations_blueprint.route("/places/<id>/delete", methods=['POST'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/places')