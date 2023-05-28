from flask import Flask,render_template
app = Flask(__name__)




@app.route("/")
def home():
    return render_template("pagina productos/index.html")

@app.route("/contacto")
def about():
    return render_template ("pagina productos/formulario.html")