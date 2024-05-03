#!/usr/bin/python3
""" Starts a Flask Web Application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from uuid import uuid4

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    st_ct = [[state, sort_cities_by_name(state)] for state in states]
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    # Generate a UUID and convert it to a string
    cache_id = str(uuid4())

    return render_template(
        '0-hbnb.html',
        states=st_ct,
        amenities=amenities,
        places=places,
        cache_id=cache_id
    )


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
