from flask import request, render_template, redirect, url_for, Blueprint, jsonify

from blueprintapp.app import db
from blueprintapp.blueprints.todos.models import Todo

# app = Flask(__name__)

# blueprint

todos = Blueprint("todos", __name__, template_folder="templates")


@todos.route("/")
def index():
    todos = Todo.query.all()
    return render_template("todos/index.html", todos=todos)


@todos.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("todos/create.html")

    elif request.method == "POST":
        title = request.form.get("title")
        description = request.form["description"]
        done = True if "done" in request.form.keys() else False

        description = description if description != "" else None

        todo = Todo(title=title, description=description, done=done)
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for("todos.index"))

@todos.route("/delete/<tid>", methods=["DELETE"])
def delete(tid):
    Todo.query.filter(Todo.tid == tid).delete()

    db.session.commit()
    people = Todo.query.all()
    
    # return redirect(url_for("people.index"))
    return jsonify({"success": True}), 200