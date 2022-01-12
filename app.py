from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "IM secret"

@app.route("/start")
def base():
	flash("Type your name....")
	return render_template("base.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", Welcome & Adios!")
	return render_template("base.html")
