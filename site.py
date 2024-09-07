from flask import Flask, render_template
from site import app as application
app = application

app = Flask(__name__)
# route => domínio do seu site, ex: /contatos, /homepage.
# função => o que você quer exibir naquela página.

# colocar o site no ar

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>") # <> => flask ler o nome de usuário
def usuarios(nome_usuario): # define a variável e joga para o html
    return render_template("usuarios.html", nome_usuario=nome_usuario) # retorna a variável descrita em html

site = app.site

if __name__ == "__main__":
    app.run(debug=True)

# colocar nosso site para pessoas acessarem
