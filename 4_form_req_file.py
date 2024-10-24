from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    Response,
    send_from_directory,
    jsonify,
)
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("file_req_4.html")
    elif request.method == "POST":
        # if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form.get("username")
        password = request.form["password"]

        if username == "okkar" and password == "flask":
            return "Success"
        else:
            return "Failure"


@app.route("/file_upload", methods=["POST"])
def file_upload():
    file = request.files["file"]

    if file.content_type == "text/plain":
        content = file.read().decode("utf-8")
        return f"<h2><pre>{content}</pre></h2>"

    elif (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        or file.content_type == "application/vnd.ms-excel"
    ):
        data_frame = pd.read_excel(file)
        table_html = data_frame.to_html(
            classes="wide-table", index=False
        )
        custom_css = """
        <style>
        .wide-table {
            width: 50%;
            border-collapse: collapse;
        }
        .wide-table th, .wide-table td {
            padding: 8px;
            border: 1px solid black;
            text-align: left;
        }
        </style>
        
        """

        return custom_css + table_html

    return (
        "<h2>Unsupported file type. Please upload a xlsx/xls or plain text file.</h2>"
    )


STATIC_FOLDER = os.path.join(app.root_path, "static", "downloads")

if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)


@app.route("/convert_csv", methods=["POST"])
def convert_csv():
    file = request.files["file"]

    df = pd.read_excel(file)
    # csv_file_path = os.path.join(STATIC_FOLDER, "result.csv")
    # df.to_csv(csv_file_path, index=False, encoding="utf-8")

    # return f"<h2>File successfully saved! <a href='/static/downloads/result.csv' download>Click here to download</a> </h2>"

    response = Response(
        df.to_csv(index=False, encoding="utf-8"),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename = result.csv"},
    )

    return response


@app.route("/convert_csv_two", methods=["POST"])
def convert_csv_two():
    file = request.files["file"]
    df = pd.read_excel(file)

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    filename = f"{uuid.uuid4()}.csv"

    df.to_csv(os.path.join("downloads", filename), index=False, encoding="utf-8")

    return render_template("download.html", filename=filename)


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("downloads", filename, download_name="result.csv")


@app.route("/handle_post", methods=["POST"])
def handle_post():
    greeting = request.json["greeting"]
    name = request.json.get("name")

    with open("file.txt", "w") as file:
        file.write(f"{greeting}, {name}!")

    return jsonify(
        # response data
        {
            "message": "Successfully written!",
            "received_data": {"greeting": greeting, "name": name},
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
