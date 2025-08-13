from flask import render_template
from igedu import app

@app.route("/login", methods=["GET", "POST"])
def login():
    return "<p>Hello, World!</p>"

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    return "<p>Hello, World!</p>"

@app.route("/matematica", methods=["GET", "POST"])
def matematica():
    return render_template('contmat.html')

@app.route("/fis", methods=["GET", "POST"])
def fis():
    return render_template('contfisica.html')

@app.route("/jog", methods=["GET", "POST"])
def jog():
    return render_template('jogos.html')

@app.route("/igor", methods=["GET", "POST"])
def igor():
    return render_template('igor.html')

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template('ICG.html')

@app.route("/algebra", methods=["GET", "POST"])
def algebra():
    return render_template('algebra.html')

@app.route("/ana", methods=["GET", "POST"])
def ana():
    return render_template('analise.html')

@app.route("/ang", methods=["GET", "POST"])
def ang():
    return render_template('Angulos.html')

@app.route("/ante", methods=["GET", "POST"])
def ante():
    return render_template('antesucessor.html')

@app.route("/base", methods=["GET", "POST"])
def base():
    return render_template('basedez.html')

@app.route("/jun", methods=["GET", "POST"])
def jun():
    return render_template('conjnum.html')

@app.route("/geom", methods=["GET", "POST"])
def geom():
    return render_template('definicaogeo.html')

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    return render_template('distanciapontos.html')

@app.route("/diz", methods=["GET", "POST"])
def diz():
    return render_template('dizimap.html')

@app.route("/equ", methods=["GET", "POST"])
def equ():
    return render_template('equacoes.html')

@app.route("/expr", methods=["GET", "POST"])
def expr():
    return render_template('expressãonum.html')

@app.route("/frac", methods=["GET", "POST"])
def frac():
    return render_template('fracoes.html')

@app.route("/matr", methods=["GET", "POST"])
def matr():
    return render_template('matrizes.html')

@app.route("/med", methods=["GET", "POST"])
def med():
    return render_template('medidas.html')

@app.route("/mmc", methods=["GET", "POST"])
def mmc():
    return render_template('mmcmdc.html')

@app.route("/nota", methods=["GET", "POST"])
def nota():
    return render_template('notaçãoc.html')

@app.route("/nun", methods=["GET", "POST"])
def nun():
    return render_template('numerosnat.html')

@app.route("/prop", methods=["GET", "POST"])
def prop():
    return render_template('proporcao.html')


@app.route("/quat", methods=["GET", "POST"])
def quat():
    return render_template('quatroop.html')


@app.route("/reg", methods=["GET", "POST"])
def reg():
    return render_template('regrade3.html')


@app.route("/sequ", methods=["GET", "POST"])
def sequ():
    return render_template('Sequencianum.html')

