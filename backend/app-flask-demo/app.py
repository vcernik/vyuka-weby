from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/backend", methods=["GET"])
def backend():
    return render_template("backend.html")

@app.route("/frontend", methods=["GET","POST"])
def frontend():
    result = None
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == "velmitajneheslo":
            result = "success"
        else:
            result = "error"
    return render_template("frontend.html", result=result)
