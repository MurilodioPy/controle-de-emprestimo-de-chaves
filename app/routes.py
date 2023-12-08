from flask import render_template, request, redirect, url_for
from . database import db # Importando a variável app do pacote app
from app import create_app
from . models import Chave, Servidor, Emprestimo

app = create_app()

# aplicando alguns teste de leitura de arquivos .css .html .js
@app.route('/')
def index():
    titulo = 'Bem-vindo ao controle de empréstimo de chavesasd'
    mensagem = 'Este é um sistema de controle de empréstimo de chaves'
    return render_template('index.html', titulo=titulo, mensagem=mensagem)

@app.route('/create', methods=['GET'])
def create_get():
    return render_template('create.html')

@app.route('/read', methods=['GET'])
def read_get():
    return render_template('read.html')

@app.route('/update', methods=['GET'])
def update_get():
    return render_template('update.html')

@app.route('/delete', methods=['GET'])
def delete_get():
    return render_template('delete.html')

# Rota para ler todas as chaves
@app.route('/read/ler', methods=['GET'])
def ler_chaves():
    chaves = Chave.query.all()
    return render_template('ler_chaves.html', chaves=chaves)

# Rota para inserir uma nova chave
@app.route('/create/inserir', methods=['POST'])
def inserir_chave():
    if request.method == 'POST':
        nome = request.form.get('nome')
        situacao = request.form.get('situacao')
        nova_chave = Chave(nome=nome, situacao=situacao)
        db.session.add(nova_chave)
        db.session.commit()
    return redirect(url_for('ler_chaves'))

# Rota para deletar uma chave
@app.route('/delete/deletar/<int:id>', methods=['POST'])
def deletar_chave(id):
    chave = Chave.query.get(id)
    if chave:
        db.session.delete(chave)
        db.session.commit()
    return redirect(url_for('ler_chaves'))

# Rota para atualizar uma chave
@app.route('/update/atualizar/<int:id>', methods=['POST'])
def atualizar_chave(id):
    chave = Chave.query.get(id)
    if chave:
        chave.nome = request.form.get('nome')
        chave.situacao = request.form.get('situacao')
        db.session.commit()
    return redirect(url_for('ler_chaves'))