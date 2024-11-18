from flask import request, render_template, redirect, url_for, Blueprint, Flask, jsonify

from blueprint_app.app import db
from blueprint_app.blueprints.people.models import Person

# app = Flask(__name__)

# blueprint

people = Blueprint("people", __name__, template_folder="templates")


@people.route("/")
def index():
    people = Person.query.all()
    return render_template("people/index.html", people=people)


@people.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("people/create.html")

    elif request.method == "POST":
        name = request.form.get("name")
        age = request.form["age"]
        job = request.form["job"]

        job = job if job != "" else None

        person = Person(name=name, age=age, job=job)
        db.session.add(person)
        db.session.commit()

        return redirect(url_for("people.index"))


@people.route("/delete/<pid>", methods=["DELETE"])
def delete(pid):
    Person.query.filter(Person.pid == pid).delete()

    db.session.commit()
    people = Person.query.all()
    
    # return redirect(url_for("people.index"))
    return jsonify({"success": True}), 200
