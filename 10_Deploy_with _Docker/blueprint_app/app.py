from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./blueprints.db"
    
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'instance', 'blueprints.db')}"

    db.init_app(app)

    # import and register all blueprints (merge all blueprints here)
    from blueprint_app.blueprints.core.routes import core
    from blueprint_app.blueprints.todos.routes import todos
    from blueprint_app.blueprints.people.routes import people

    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(people, url_prefix="/people")

    migrate = Migrate(app, db)

    return app
