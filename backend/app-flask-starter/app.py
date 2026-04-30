from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
import csv
from pathlib import Path

app = Flask(__name__)
app.secret_key = "daijfgaopjgagew"

# CSV log file path
LOG_FILE = Path(app.root_path) / "logins.csv"


def log_login(name, result):
	try:
		write_header = not LOG_FILE.exists()
		with LOG_FILE.open("a", encoding="utf-8", newline="") as f:
			writer = csv.writer(f)
			if write_header:
				writer.writerow(["datetime", "name", "result"])
			writer.writerow([datetime.now().isoformat(sep=' '), name or "", result])
	except Exception:
		# Never raise from logging to avoid breaking the app
		pass


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


	name = request.form.get("name")
	surname = request.form.get("surname")
	password = request.form.get("password")
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

	# If this is a POST, treat it as a login attempt and log it
	if request.method == "POST":
		result = "OK" if password == "heslo" else "FAIL"
		log_login(name or "", result)
		if result == "OK":
			session["password"] = password
		else:
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

 
