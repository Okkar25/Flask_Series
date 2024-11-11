from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# to mange cookies
# 1. saved cookies from first request and use it in second request
# 2. use session instead

# * check main.py
# sending request from main.py 


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()  # to Dict Format
    username = data.get("username")
    password = data.get("password")

    if username == "testuser" and password == "testpass":
        res = make_response(
            jsonify(success=True)
        )  # {'success': True} # into a JSON response
        res.set_cookie("session", "logged_in")
        return res
    else:
        return jsonify(success=False), 401  # {'success': False}


@app.route("/protected")
def protected():
    session_cookie = request.cookies.get("session")
    if session_cookie == "logged_in":
        return jsonify(access=True)
    else:
        return jsonify(access=False), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
