from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entrar')
def entrar():
  return render_template('entrar.html')

@app.route('/contato')
def contato():
  return render_template('contato.html')

@app.route('/avaliacao')
def avaliacao():  
  return render_template('avaliacao.html')

@app.route('/avaliacoes', methods=["GET", "POST"])
def avaliacoes():
  nome = request.form.get('nome')
  mensagem = request.form.get('mensagem')
  return "{}: {}".format(nome, mensagem)
  
  return render_template('avaliacoes.html')

app.run(host='0.0.0.0', port=81)