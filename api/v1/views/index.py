#!/usr/bin/python3xx
'''function to execute the flask api status
'''

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def stat_return():
    """ a function that return the datababse status """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat_count():
    """ a function that return the count of datababse status """
    count_stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(count_stats)


if __name__ == "__main__":
    pass
