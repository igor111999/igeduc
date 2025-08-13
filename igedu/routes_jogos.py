from flask import render_template
from igedu import app

@app.route("/multip", methods=["GET", "POST"])
def multip():
    return render_template('templates_jogos/jogomult.html')

@app.route("/multi", methods=["GET", "POST"])
def multi():
    return render_template('templates_jogos/mult.html')

@app.route("/divi", methods=["GET", "POST"])
def divi():
    return render_template('templates_jogos/div.html')

@app.route("/adic", methods=["GET", "POST"])
def adic():
    return render_template('templates_jogos/adic.html')

@app.route("/sub", methods=["GET", "POST"])
def sub():
    return render_template('templates_jogos/sub.html')

@app.route("/velha", methods=["GET", "POST"])
def velha():
    return render_template('templates_jogos/velha.html')

@app.route("/racio", methods=["GET", "POST"])
def racio():
    return render_template('templates_jogos/racio.html')