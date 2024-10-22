from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd

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
        table_html = data_frame.to_html(classes="wide-table", index=False)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
