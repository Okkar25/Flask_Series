from blueprint_app.app import db


class Person(db.Model):
    __tablename__ = "people"

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String)

    def __repr__(self):
        return f"< Person: {self.name}, Age: {self.age}, Job: {self.job} >"

    def get_id(self):
        return self.pid
