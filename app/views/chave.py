from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Chave
from ..database import db

chave_bp = Blueprint('chave', __name__, template_folder='templates', url_prefix='/')

@chave_bp.route('/')
def index():
    return render_template('index.html')

@chave_bp.route('/create/chave', methods=['GET'])
def create_get():
    return render_template('chave/createChave.html')

@chave_bp.route('/read/chave', methods=['GET'])
def read_get():
    return render_template('chave/readChave.html')

@chave_bp.route('/update/chave', methods=['GET'])
def update_get():
    return render_template('chave/updateChave.html')

@chave_bp.route('/delete/chave', methods=['GET'])
def delete_get():
    return render_template('chave/deleteChave.html')

# Rota para ler todas as chaves
@chave_bp.route('/read/chaves', methods=['GET'])
def mostrarChaves():
    chaves = Chave.query.all()
    return render_template('chave/mostrarChaves.html', chaves=chaves)

# Rota para inserir uma nova chave
@chave_bp.route('/createRequest/', methods=['POST'])
def inserir_chave():
    if request.method == 'POST':
        nome = request.form.get('nome')
        situacao = request.form.get('situacao')
        nova_chave = Chave(nome=nome, situacao=situacao)
        db.session.add(nova_chave)
        db.session.commit()
    return redirect(url_for('chave.mostrarChaves'))

# Rota para deletar uma chave
@chave_bp.route('/deleteRequest', methods=['POST'])
def deletar_chave():
    id = request.form.get('id')
    if id:
        chave = Chave.query.get(id)
        if chave:
            db.session.delete(chave)
            db.session.commit()
    return redirect(url_for('chave.mostrarChaves'))

# Rota para atualizar uma chave
@chave_bp.route('/updateRequest', methods=['POST'])
def atualizar_chave():
    id = request.form.get('id')
    if id:
        chave = Chave.query.get(id)
        if chave:
            chave.nome = request.form.get('nome')
            chave.situacao = request.form.get('situacao')
            db.session.commit()
    return redirect(url_for('chave.mostrarChaves'))