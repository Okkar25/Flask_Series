from flask import render_template, Blueprint


# blueprint

core = Blueprint("core", __name__, template_folder="templates")


@core.route("/")
def index():
    return render_template("core/index.html")
