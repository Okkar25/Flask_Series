from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./testdb.db"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Postgres081922@localhost:5433/people_db"

    db.init_app(app)

    # imports
    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)
    
    return app
