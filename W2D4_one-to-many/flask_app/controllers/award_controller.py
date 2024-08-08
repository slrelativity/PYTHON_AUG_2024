# contoller is for routing
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.award_model import Award
from flask_app.models.dog_model import Dog

# -------------- CREATE AWARD (RENDER/DISPLAY) PAGE
# /tablename/id/action
@app.route("/awards/new")
def create_award_page():
    all_dogs = Dog.get_all()
    return render_template("award_new.html",
                           all_dogs=all_dogs)

# ----------- CREATE METHOD - ACTION
@app.route("/awards/create", methods=['post'])
def make_an_award_action():
    print("\n\n********* >>>\n\n", request.form)
    Award.create(request.form)
    return redirect("/awards/new")