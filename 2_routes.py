from flask import Flask, render_template, request, make_response
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello World</h1>"


@app.route("/hello")
def hello():
    return "<h2>Hello, This is Flask App</h2>", 202  # custom request


@app.route("/make_res")
def make_res():
    response = make_response("Make Response\n")
    response.status_code = 202
    response.headers["content-type"] = "application/octet-stream"
    return response


@app.route("/about", methods=["GET", "POST", "DELETE", "PUT"])
def about():
    if request.method == "GET":
        return "This is About Page - GET\n"
    elif request.method == "POST":
        return "This is About Page - POST\n"
    else:
        return "You will never see this message\n"


@app.route("/greet/<name>")  # url processor
def greet(name):
    # return f"Hello {name}"
    return f"<h1>Hello {name}</h1>"


# @app.route("/add/<number1>/<number2>")
# def add(number1, number2):
#     number1 = int(number1)
#     number2 = int(number2)
#     return f"<h1>{number1} + {number2} = {number1 + number2}</h1>"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"<h1>{number1} + {number2} = {number1 + number2}</h1>"


# /handle_url_params?name="John"&greetings=Bonjour => ImmutableMultiDict([('name', 'John'), ('greetings', 'Bonjour')])
@app.route("/handle_url_params")
def handle_params():
    # return request.args
    # return str(request.args)
    if "greetings" in request.args.keys() and "name" in request.args.keys():
        greetings = request.args["greetings"]
        name = request.args.get("name")
        return f"<h2>{greetings}, {name} !</h2>"
    else:
        return "Some parameters are missing!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    # serve(app, host="0.0.0.0", port=8000 )
