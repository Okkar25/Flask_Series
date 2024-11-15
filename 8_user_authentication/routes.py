from models import User
from flask import request, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required


def register_routes(app, db, bcrypt):
    @app.route("/")
    def index():
        # if current_user.is_authenticated:
        #     return str(current_user.username)
        # else:
        #     return "No user is logged in"

        return render_template("index.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "GET":
            return render_template("signup.html")
        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            # Check if username already exists
            if User.query.filter_by(username=username).first():
                return "This username already exists!"

            hashed_password = bcrypt.generate_password_hash(password)

            user = User(username=username, password=hashed_password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for("index"))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            return render_template("login.html")
        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            user = User.query.filter(User.username == username).first()

            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                # return render_template("index.html")
                return redirect(url_for("index"))
            else:
                return "Login Failed!"

    # @app.route("/login/<uid>")
    # def login(uid):
    #     user = User.query.get(uid)
    #     login_user(user)
    #     return "Login Successful"

    @app.route("/logout")
    def logout():
        logout_user()
        # return "Logout Successful"
        return redirect(url_for("index"))

    @app.route("/secret")
    @login_required
    def secret():
        # if current_user.is_authenticated and current_user.role == "admin":
        if current_user.is_authenticated:
            return "You are logged in as Admin"
        else:
            return "You are not authorized as Admin"

    # def secret():
    #     if current_user.role == "admin":
    #         return "This is Admin"
    #     else:
    #         return "No Permission"
