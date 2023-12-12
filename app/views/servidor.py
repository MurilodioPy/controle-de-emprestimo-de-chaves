from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError, OperationalError
from datetime import datetime
from ..models import Servidor
from ..database import db


servidor_bp = Blueprint('servidor', __name__, template_folder='templates')

@servidor_bp.route('/')
def index():
    servidores = Servidor.query.all()
    return render_template('servidor/index.html', servidores=servidores)

@servidor_bp.route('/create', methods=['GET'])
def create_get():
    return render_template('servidor/createServidor.html')

@servidor_bp.route('/update', methods=['GET'])
def update_get():
    servidores = Servidor.query.all()
    return render_template('servidor/updateServidor.html', servidores=servidores)

@servidor_bp.route('/delete', methods=['GET'])
def delete_get():
    servidores = Servidor.query.all()
    return render_template('servidor/deleteServidor.html', servidores=servidores)

# Rota para inserir um novo servidor
@servidor_bp.route('/createRequest', methods=['POST'])
def inserir_servidor():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    contato = request.form.get('contato')
    nascimento_str = request.form.get('nascimento')
    nascimento = datetime.strptime(nascimento_str, '%Y-%m-%d').date()
    status = request.form.get("status")
    
    try:
            # Criar um novo objeto Servidor e adicioná-lo ao banco de dados
            novo_servidor = Servidor(
                nome=nome,
                cpf=cpf,
                contato=contato,
                nascimento=nascimento,
                status=status
            )

            db.session.add(novo_servidor)
            db.session.commit()

    except OperationalError as e:
        # Trate o erro de formato de data incorreto aqui
        print(f"Erro de formato de data: {e}")
        return render_template('error/erro_cpf.html')

    except IntegrityError as e:
        # Trate a violação de integridade (CPF duplicado) aqui
        print(f"Erro de integridade: {e}")
        return render_template('error/erro_data.html')  # Substitua pelo seu template de erro
    flash("Servidor inserido com sucesso!")
    return redirect(url_for('servidor.index'))

# Rota para deletar uma chave
@servidor_bp.route('/deleteRequest', methods=['POST'])
def deletar_servidor():
    id_servidor = request.form.get('id')
    if id_servidor:
        servidor = Servidor.query.get(id_servidor)
        if servidor:
            if servidor.status == "Sem Pendencia":
                db.session.delete(servidor)
                db.session.commit()
    flash("Servidor removido com sucesso!")
    return redirect(url_for('servidor.index'))

# Rota para atualizar uma chave
@servidor_bp.route('/updateRequest', methods=['POST'])
def atualizar_servidor():
    id = request.form.get('id')
    if id:
        servidor = Servidor.query.get(id)
        if servidor:
            if servidor.status == "Sem Pendencia":
                if nome := request.form.get('nome'):
                    servidor.nome = nome
                if cpf := request.form.get('cpf'):
                    servidor.cpf = cpf
                if contato := request.form.get('contato'):
                    servidor.contato = contato
                if nascimento := request.form.get('nascimento'):
                    servidor.nascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
                try:        
                        db.session.commit()
                except OperationalError as e:
                # Trate o erro de formato de data incorreto aqui
                    print(f"Erro de formato de data: {e}")
                    return render_template('error/erro_cpf.html')
                
                except IntegrityError as e:
                # Trate a violação de integridade (CPF duplicado) aqui
                    print(f"Erro de integridade: {e}")
                    return render_template('error/erro_data.html')
                flash("Servidor atualizado com sucesso!")
            else:
                flash("Servidor com pendência!")
    return redirect(url_for('servidor.index'))