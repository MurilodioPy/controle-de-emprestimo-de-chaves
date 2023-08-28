from flask import render_template  # Importe render_template
from app import app

# aplicando alguns teste de leitura de arquivos .css .html .js
@app.route('/')
def index():
    titulo = 'Bem-vindo ao controle de empréstimo de chaves'
    mensagem = 'Este é um sistema de controle de empréstimo de chaves!'
    return render_template('index.html', titulo=titulo, mensagem=mensagem)

@app.route('/about')
def sobre():
    return "<h1>Sobre o sistema</h1>"

@app.route('/usuarios')
def users():
    return "<h1>Usuários</h1>"

@app.route('/chaves')
def chave():
    return "<h1>Chaves</h1>"