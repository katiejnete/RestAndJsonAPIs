"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect, request, flash
from flask import jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)
app.app_context().push()

@app.route("/")
def home_page():
    """Shows cupcakes list and form for adding new cupcakes."""
    return render_template("home.html")

@app.route("/api/cupcakes")
def get_cupcakes():
    """Get data about all cupcakes."""

    cupcakes = db.session.execute(db.select(Cupcake)).scalars()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Get data about single cupcake."""

    cupcake = db.get_or_404(Cupcake, cupcake_id)

    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create cupcake."""

    try:
        new_cupcake = Cupcake(
            flavor=request.json["flavor"],
            size=request.json["size"],
            rating=request.json["rating"],
            image=request.json.get("image", None),
        )
        db.session.add(new_cupcake)
        db.session.commit()
        response_json = jsonify(cupcake=new_cupcake.serialize())
        return (response_json, 201)
    except:
        response_json = jsonify(message="not created")
        return (response_json, 404)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake."""

    try:
        cupcake = db.get_or_404(Cupcake, cupcake_id)
        cupcake.flavor = request.json.get("flavor", cupcake.flavor)
        cupcake.size = request.json.get("size", cupcake.size)
        cupcake.rating = request.json.get("rating", cupcake.rating)
        cupcake.image = request.json.get("image", cupcake.image)
        db.session.commit()
        return jsonify(cupcake=cupcake.serialize())
    except:
        response_json = jsonify(message="not updated")
        return (response_json, 404)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete cupcake."""

    cupcake = db.get_or_404(Cupcake, cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")