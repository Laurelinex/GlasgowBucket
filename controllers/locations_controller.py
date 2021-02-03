from flask import Flask, Blueprint, render_template, redirect, request

from models.location import Location

import repositories.location_repository as location_repository
import repositories.zone_repository as zone_repository
import repositories.category_repository as category_repository

locations_blueprint = Blueprint("locations", __name__)

# Locations index page
@locations_blueprint.route("/places")
def locations():
    zones = zone_repository.select_all()
    categories = category_repository.select_all()
    locations = location_repository.select_all()
    return render_template('locations/index.html', all_locations = locations, all_zones = zones, all_categories = categories)

# Show a specific place
@locations_blueprint.route("/places/<id>", methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    return render_template('locations/show.html', location = location)

# Add new place page
@locations_blueprint.route("/places/new")
def new_location():
    zones = zone_repository.select_all()
    categories = category_repository.select_all()
    locations = location_repository.select_all()
    return render_template('locations/new.html', all_zones = zones, all_categories = categories, all_locations = locations)

# Create new place
@locations_blueprint.route("/places", methods=['POST'])
def create_location():
    name = request.form['name']
    address = request.form['address']
    description = request.form['description']
    zone_id = request.form['zone_id']
    category_id = request.form['category_id']
    picture = request.form['picture']
    lockdown_friendly = request.form['lockdown_friendly']
    free = request.form['free']
    visited = request.form['visited']
    zone = zone_repository.select(zone_id)
    category = category_repository.select(category_id)
    location = Location(name, address, description, zone, category, picture, lockdown_friendly, free, visited)
    location_repository.save(location)
    return redirect('/places')

# Edit place page
@locations_blueprint.route("/places/<id>/edit", methods=['GET'])
def edit_location(id):
    location = location_repository.select(id)
    zones = zone_repository.select_all()
    categories = category_repository.select_all()
    return render_template('locations/edit.html', location = location, all_zones = zones, all_categories = categories)

# Update place info
@locations_blueprint.route("/places/<id>", methods=['POST'])
def update_location(id):
    name = request.form['name']
    address = request.form['address']
    description = request.form['description']
    zone = request.form['zone_id']
    category = request.form['category_id']
    picture = request.form['picture']
    lockdown_friendly = request.form['lockdown_friendly']
    free = request.form['free']
    visited = request.form['visited']
    zone = zone_repository.select(request.form['zone_id'])
    category = category_repository.select(request.form['category_id'])
    location = Location(name, address, description, zone, category, picture, lockdown_friendly, free, visited, id)
    location_repository.update(location)
    return redirect('/places')

# Delete place
@locations_blueprint.route("/places/<id>/delete", methods=['POST'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/places')

# Show a list of filtered places by zone
@locations_blueprint.route("/places/filter_zone/<zone_id>", methods=['GET'])
def show_filtered_locations_by_zone(zone_id):
    zone = zone_repository.select(zone_id)
    locations = location_repository.select_by_zone(zone)
    return render_template('locations/filtered_zone.html', filtered_locations = locations, zone = zone)

# Show a list of filtered places by category
@locations_blueprint.route("/places/filter_category/<category_id>", methods=['GET'])
def show_filtered_locations_by_category(category_id):
    category = category_repository.select(category_id)
    locations = location_repository.select_by_category(category)
    return render_template('locations/filtered_category.html', filtered_locations = locations, category = category)

# Show a list of filtered places by status (visited True/False)
@locations_blueprint.route("/places/filter_visited/<visited>", methods=['GET'])
def show_filtered_locations_by_status(visited):
    locations = location_repository.select_by_visited(visited)
    return render_template('locations/filtered_status.html', filtered_locations = locations)

# Show a list of filtered places by lockdown friendliness (lockdown friendly True/False)
@locations_blueprint.route("/places/filter_lockdown/<lockdown_friendly>", methods=['GET'])
def show_filtered_locations_by_lockdown_friendliness(lockdown_friendly):
    locations = location_repository.select_by_lockdown_friendliness(lockdown_friendly)
    return render_template('locations/filtered_lockdown.html', filtered_locations = locations)

# Show a list of filtered places by entry fee (free True/False)
@locations_blueprint.route("/places/filter_free/<free>", methods=['GET'])
def show_filtered_locations_by_free_entry(free):
    locations = location_repository.select_by_free_entry(free)
    return render_template('locations/filtered_free.html', filtered_locations = locations)