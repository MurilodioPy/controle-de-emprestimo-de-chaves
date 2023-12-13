from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import Chave
from ..database import db

chave_bp = Blueprint('chave', __name__, template_folder='templates')

@chave_bp.route('/')
def index():
    chaves = Chave.query.all()
    return render_template('chave/index.html', chaves=chaves)

@chave_bp.route('/create', methods=['GET'])
def create_get():
    return render_template('chave/createChave.html')

@chave_bp.route('/read', methods=['GET'])
def readKey_get():
    return render_template('chave/buscarChave.html')

@chave_bp.route('/update', methods=['GET'])
def update_get():
    chaves = Chave.query.all()
    return render_template('chave/updateChave.html', chaves=chaves)

@chave_bp.route('/delete', methods=['GET'])
def delete_get():
    chaves = Chave.query.filter_by(status='disponivel').all()
    return render_template('chave/deleteChave.html', chaves=chaves)

@chave_bp.route('/readRequest', methods=['POST', 'GET'])
def buscar_chave():
    if request.method == 'POST':
        nome_str = request.form.get('nome')
        if nome_str:
            chaves = Chave.query.filter(Chave.nome.ilike(f'%{nome_str}%')).all()
    return render_template('chave/buscarChave.html', chaves=chaves)

# Rota para inserir uma nova chave
@chave_bp.route('/createRequest', methods=['POST'])
def inserir_chave():
    if request.method == 'POST':
        nome = request.form.get('nome')
        situacao = request.form.get('situacao')
        nova_chave = Chave(nome=nome, situacao=situacao)
        db.session.add(nova_chave)
        db.session.commit()
    flash("Chave inserida com sucesso")
    return redirect(url_for('chave.index'))

# Rota para deletar uma chave
@chave_bp.route('/deleteRequest', methods=['POST'])
def deletar_chave():
    id = request.form.get('id')
    if id:
        chave = Chave.query.get(id)
        if chave:
            db.session.delete(chave)
            db.session.commit()
    flash("Chave deletada com sucesso")
    return redirect(url_for('chave.index'))

# Rota para atualizar uma chave
@chave_bp.route('/updateRequest', methods=['POST'])
def atualizar_chave():
    id = request.form.get('id')
    if id:
        chave = Chave.query.get(id)
        if chave:
            if nome := request.form.get('nome'):
                chave.nome = nome 
            if situacao := request.form.get('situacao'):
                chave.situacao = situacao
            db.session.commit()
    flash("Chave atualizada com sucesso")
    return redirect(url_for('chave.index'))


def atualizar_status_chave(chave_id):
        # Atualizar o status da chave para "Indisponível" ou "Disponível"
        chave = Chave.query.get(chave_id)
        if chave:
            if chave.status == 'disponivel':
                chave.status = 'indisponivel'
                return True
            else:
                chave.status = 'disponivel'
            db.session.commit()
            
def status_chave(chave_id):
    chave = Chave.query.get(chave_id)
    if chave:
        if chave.status == 'disponivel':
            return True
        else:
            return False
    else:
        return False

