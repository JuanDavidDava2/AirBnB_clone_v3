#!/usr/bin/python3
""" init flask files """

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    """ return status """
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def objs_counter():
    """return total count of each obj per class"""
    classes = {"amenities": "Amenity", 
               "cities": "City",
               "places": "Place",
               "reviews": "Review",
               "states": "State",
               "users": "User"}
    classes_dic = {}
    for item, val in classes.items():
        classes[item] = storage.count(eval(val))
    return jsonify(classes_dic)
