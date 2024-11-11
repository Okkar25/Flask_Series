from flask import request, render_template
from models import Person


def register_routes(app, db):
    @app.route("/", methods=["POST", "GET"])
    def index():
        if request.method == "GET":
            people = Person.query.all()
            # return str(people)
            return render_template("index.html", people=people)

        elif request.method == "POST":
            name = request.form["name"]
            age = int(request.form["age"])
            job = request.form.get("job")
            major = request.form.get("major")

            # adding person data into database
            person = Person(name=name, age=age, job=job, major=major)
            db.session.add(person)
            # db.session.flush()  # Ensure the new entry is available for querying immediately
            db.session.commit()  # saved in database

            people = Person.query.all()
            return render_template("index.html", people=people)

    @app.route("/delete/<pid>", methods=["DELETE"])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()

        db.session.commit()  # saved in database

        people = Person.query.all()
        return render_template("index.html", people=people)
