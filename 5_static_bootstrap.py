from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(
    __name__, template_folder="templates", static_folder="static", static_url_path="/"
)
Bootstrap(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("static_bootstrap_5.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
