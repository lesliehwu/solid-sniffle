from flask import Flask, render_template, redirect, request, session, flash, url_for
app = Flask(__name__)
app.secret_key = 'BillsLocalHost'

@app.route("/")
def index():
    return render_template("color.html", couleur = "lightyellow")

@app.route("/color", methods=['POST','GET'])
def color():

    reds = request.form['reds']
    greens = request.form['greens']
    blues = request.form['blues']
    
    couleur = "rgb(" + str(reds) + ", " + str(greens) + ", " + str(blues) + ")"

    return render_template("color.html",couleur = couleur)


app.run(debug = True)
