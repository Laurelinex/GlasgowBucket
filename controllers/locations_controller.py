from flask import Flask, Blueprint, render_template

from models.location import Location

import repositories.location_repository as location_repository

locations_blueprint = Blueprint("locations", __name__)