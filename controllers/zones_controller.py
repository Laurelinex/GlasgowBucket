from flask import Flask, Blueprint, render_template

from models.zone import Zone

import repositories.zone_repository as zone_repository

zones_blueprint = Blueprint("zones", __name__)