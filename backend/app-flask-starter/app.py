from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "daijfgaopjgagew"


@app.route("/", methods=["GET"])
def index():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")

	name = request.args.get("name")
	surname = request.args.get("surname")

	return render_template("page.html", date=date, name=name, surname=surname)

@app.route("/pozdrav-post", methods=["GET", "POST"])
def pozdrav_post():
	#aktuální datum
	date = datetime.now().strftime("%d. %m. %Y")


	name=request.form.get("name")
	surname=request.form.get("surname")
	password=request.form.get("password")
	session["password"] = password
	message = None


	if name is None or len(name) > 50:
		name = None
		message = "Neplatné jméno!"

	if surname is None or len(surname) > 50:
		surname = None
		message = "Neplatné příjmení!"

	if password is None or len(password) > 50:
		password = None
		message = "Neplatné heslo!"

	return render_template("pozdrav_post.html", date=date, name=name, surname=surname, password=password, message=message)

@app.route("/tajne", methods=["GET", "POST"])
def tajne():
	session_password = session.get("password")
	if session_password != "heslo":
		return redirect(url_for("pozdrav_post", message="Neplatné heslo!", date=datetime.now().strftime("%d. %m. %Y")))
	else:
		return render_template("tajne.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


if __name__ == "__main__":
	app.run(debug=True)

 
