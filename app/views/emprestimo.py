from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Emprestimo
from ..database import db

emprestimo_bp = Blueprint('emprestimo', __name__, template_folder='templates')

@emprestimo_bp.route('/')
def index():
    return render_template('emprestimo/index.html')

@emprestimo_bp.route('/create', methods=['GET'])
def create_get():
    return render_template('emprestimo/createEmprestimo.html')

@emprestimo_bp.route('/update', methods=['GET'])
def update_get():
    return render_template('emprestimo/updateEmprestimo.html')

@emprestimo_bp.route('/delete', methods=['GET'])
def delete_get():
    return render_template('emprestimo/deleteEmprestimo.html')

@emprestimo_bp.route('/createRequest', methods=['POST'])
def inserir_emprestimo():
    if request.method == 'POST':
        # Obter dados do formulário
        datahora_emprestimo = request.form.get('datahora_emprestimo')
        datahora_devolucao = request.form.get('datahora_devolucao')
        status = request.form.get('status')
        chave_id = request.form.get('chave_id')
        servidor_retirou_id = request.form.get('servidor_retirou_id')
        servidor_devolveu_id = request.form.get('servidor_devolveu_id')

        # Criar um novo objeto Emprestimo e adicioná-lo ao banco de dados
        novo_emprestimo = Emprestimo(
            datahora_emprestimo=datahora_emprestimo,
            datahora_devolucao=datahora_devolucao,
            status=status,
            chave_id=chave_id,
            servidor_retirou_id=servidor_retirou_id,
            servidor_devolveu_id=servidor_devolveu_id
        )

        db.session.add(novo_emprestimo)
        db.session.commit()

    return redirect(url_for('emprestimo.mostrar_emprestimos'))

@emprestimo_bp.route('/deleteRequest', methods=['POST'])
def deletar_emprestimo():
    if request.method == 'POST':
        # Obter o ID do empréstimo a ser deletado
        emprestimo_id = request.form.get('id')
        # Obter o empréstimo pelo ID
        emprestimo = Emprestimo.query.get(emprestimo_id)
        if emprestimo:
            # Deletar o empréstimo do banco de dados
            db.session.delete(emprestimo)
            db.session.commit()

    return redirect(url_for('emprestimo.mostrar_emprestimos'))

@emprestimo_bp.route('/updateRequest', methods=['POST'])
def atualizar_emprestimo():
    emprestimo_id = request.form.get('id')
    if emprestimo_id:
        emprestimo = Emprestimo.query.get(emprestimo_id)
        if emprestimo:
            if datahora_emprestimo := request.form.get('datahora_emprestimo'):
                emprestimo.datahora_emprestimo = datahora_emprestimo
            if datahora_devolucao := request.form.get('datahora_devolucao'):
                emprestimo.datahora_devolucao = datahora_devolucao
            if status := request.form.get('status'):
                emprestimo.status = status
            if chave_id := request.form.get('chave_id'):
                emprestimo.chave_id = chave_id
            if servidor_retirou_id := request.form.get('servidor_retirou_id'):
                emprestimo.servidor_retirou_id = servidor_retirou_id
            if servidor_devolveu_id := request.form.get('servidor_devolveu_id'):
                emprestimo.servidor_devolveu_id = servidor_devolveu_id

            db.session.commit()

    return redirect(url_for('emprestimo.ler_emprestimos'))


@emprestimo_bp.route('/read', methods=['GET'])
def mostrar_emprestimos():
    emprestimos = Emprestimo.query.all()
    return render_template('emprestimo/mostrarEmprestimos.html', emprestimos=emprestimos)
