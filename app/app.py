from flask import Flask,render_template, request, redirect
app = Flask(__name__)
usuario = []




@app.route("/")
def home():
    return render_template("pagina productos/index.html")

@app.route("/contacto", methods =["GET", "POST"])
def contacto():
    if request.method == "POST":
        usuario.append(request.form)
        return redirect("/user")
    return render_template ("pagina productos/formulario.html")

@app.route("/user")
def user():
    return render_template("pagina productos/user.html", usuario = usuario)