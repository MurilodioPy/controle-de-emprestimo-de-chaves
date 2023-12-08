from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Servidor
from ..database import db

servidor_bp = Blueprint('servidor', __name__, template_folder='templates')

@servidor_bp.route('/')
def index():
    return render_template('index.html')

@servidor_bp.route('/create/servidor', methods=['GET'])
def create_get():
    return render_template('servidor/createServidor.html')

@servidor_bp.route('/read/servidor', methods=['GET'])
def read_get():
    return render_template('servidor/readServidor.html')

@servidor_bp.route('/update/servidor', methods=['GET'])
def update_get():
    return render_template('servidor/updateServidor.html')

@servidor_bp.route('/delete/servidor', methods=['GET'])
def delete_get():
    return render_template('servidor/deleteServidor.html')

# Rota para ler todas as chaves
@servidor_bp.route('/read/servidor', methods=['GET'])
def ler_servidores():
    servidores = Servidor.query.all()
    return render_template('servidor/mostrarServidores.html', servidores=servidores)

# Rota para inserir uma nova chave
@servidor_bp.route('/createRequest', methods=['POST'])
def inserir_servidor():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    contato = request.form.get('contato')
    nascimento = request.form.get('nascimento')
    status = request.form.get('status')

    novo_servidor = Servidor(nome=nome, cpf=cpf, contato=contato, nascimento=nascimento, status=status)
    db.session.add(novo_servidor)
    db.session.commit()

    return redirect(url_for('servidor.ler_servidores'))

# Rota para deletar uma chave
@servidor_bp.route('/deleteRequest', methods=['POST'])
def deletar_servidor():
    id_servidor = request.form.get('id')
    if id_servidor:
        servidor = Servidor.query.get(id_servidor)
        if servidor:
            db.session.delete(servidor)
            db.session.commit()

    return redirect(url_for('servidor.ler_servidores'))

# Rota para atualizar uma chave
@servidor_bp.route('/updateRequest', methods=['POST'])
def atualizar_servidor():
    id = request.form.get('id')
    if id:
        servidor = Servidor.query.get(id)
        if servidor:
            if nome := request.form.get('nome'):
                servidor.nome = nome
            if cpf := request.form.get('cpf'):
                servidor.cpf = cpf
            if contato := request.form.get('contato'):
                servidor.contato = contato
            if nascimento := request.form.get('nascimento'):
                servidor.nascimento = nascimento
            if status := request.form.get('status'):
                servidor.status = status
            db.session.commit()
    return redirect(url_for('servidor.ler_servidores'))