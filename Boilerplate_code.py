#Importando o módulo flask no projeto
from flask import Flask, render_template

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/")

# A URL ‘/’ é ligada à função first_flask.
def first_flask():
    cor = "verde"
    maiorMedo = "gatos da cor azul"
    return render_template("onomiquevcquiser.html", cor=cor, maiorMedo=maiorMedo)

# Execute a aplicação no servidor local
app.run()

