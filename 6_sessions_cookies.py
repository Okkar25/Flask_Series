from flask import Flask, render_template, request, session, make_response, flash

app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "SOME_SECRET_KEY"


@app.route("/")
@app.route("/index")
def index():
    return render_template("sessions_cookies_6.html", message="Index Data")


@app.route("/set_session")
def set_session():
    session["name"] = "Noobmaster69"
    session["code"] = "RTX4302SOF"
    return render_template(
        "sessions_cookies_6.html", session_message="Session Data Set"
    )


@app.route("/get_session")
def get_session():
    if "name" in session.keys() and "code" in session.keys():
        name = session["name"]
        code = session["code"]
        return render_template(
            "sessions_cookies_6.html",
            session_message=f"Name : {name} and Code : {code}",
        )
    else:
        return render_template(
            "sessions_cookies_6.html", session_message="There is no Session Data :("
        )


@app.route("/clear_session")
def clear_session():
    # clearing every session data
    session.clear()

    # clearing specific session data
    # session.pop("name")
    # session.pop("code")

    return render_template(
        "sessions_cookies_6.html", session_message="Session Data Cleared :)"
    )


@app.route("/set_cookie")
def set_cookie():
    response = make_response(
        render_template("sessions_cookies_6.html", cookie_message="Cookie Data Set")
        # "Cookie Data Set"
    )

    response.set_cookie(
        "cookie_name",
        "My favorite cookie is HTTP Cookie",
        max_age=60 * 1,  # Expire after One minute
    )
    return response


@app.route("/get_cookie")
def get_cookie():
    if "cookie_name" in request.cookies:
        cookie_value = request.cookies["cookie_name"]
        return render_template(
            "sessions_cookies_6.html", cookie_message=f"Cookie Value : {cookie_value}"
        )
    else:
        return render_template(
            "sessions_cookies_6.html", cookie_message="There is no Cookies Data :("
        )


@app.route("/remove_cookie")
def remove_cookie():
    response = make_response(
        render_template(
            "sessions_cookies_6.html", cookie_message="Cookie Data Cleared :)"
        )
    )
    response.set_cookie("cookie_name", expires=0)
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form.get("password")

        if username == "okkar" and password == "open123":
            flash("Successful Login!")
            return render_template("sessions_cookies_6.html", my_message="")
        else:
            flash("Login Failed")
            return render_template("sessions_cookies_6.html", my_message="")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
