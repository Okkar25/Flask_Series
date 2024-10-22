from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")


@app.route("/")
@app.route("/index")
def index():
    my_list = ["John", "Sarah", "Bobby", "Deborah", "Jane", "Daisy", "David", "Max"]
    my_value = "Jupyter 11"
    return render_template("index.html", my_list=my_list, my_value=my_value)


@app.route("/other")
def other():
    my_fruits = ["apple", "orange", "peach", "grape", "banana"]
    some_text = "some text"
    alter_text = "This Is HOLLYWOOD."
    return render_template(
        "other.html", my_fruits=my_fruits, some_text=some_text, alter_text=alter_text
    )


# redirect
@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(
        url_for("other")  # finds other function and go to that respective route
    )


# custom jinja filters
@app.template_filter("reverse_string")
def reverse_string(value):
    return value[::-1]


@app.template_filter("repeat")
def repeat(str, times=2):
    # return str * times
    return " _ ".join(
        [str] * times
    )  # "some text" => ["some text"] * 2 => ["some text", "some text"]


@app.template_filter("alternate_case")
def alternate_case(str):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(str)])


@app.template_filter("swap_case")
def swap_case(str):
    return "".join([c.upper() if c.islower() else c.lower() for c in str])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
