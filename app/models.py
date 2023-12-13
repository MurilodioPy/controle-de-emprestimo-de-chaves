from datetime import datetime, date
from . database import db
from sqlalchemy import Date

class Chave(db.Model):
   __tablename__ = 'chaves'
   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(255), nullable=False)
   situacao = db.Column(db.String(255), nullable=False)
   status = db.Column(db.String(255), default='disponivel')

class Servidor(db.Model):
   __tablename__ = 'servidores'
   id = db.Column(db.Integer, primary_key=True)
   nome = db.Column(db.String(255), nullable=False)
   cpf = db.Column(db.String(255), unique=True, nullable=False)
   contato = db.Column(db.String(255))
   nascimento = db.Column(Date)
   status = db.Column(db.String(255), default='Sem Pendencia')

class Emprestimo(db.Model):
   __tablename__ = 'emprestimos'
   id = db.Column(db.Integer, primary_key=True)
   datahora_emprestimo = db.Column(db.DateTime, default=datetime.utcnow())
   datahora_devolucao = db.Column(db.DateTime)
   status = db.Column(db.String(255), default='Ativo')
   chave_id = db.Column(db.Integer, db.ForeignKey('chaves.id'))
   servidor_retirou_id = db.Column(db.Integer, db.ForeignKey('servidores.id'))
   servidor_devolveu_id = db.Column(db.Integer, db.ForeignKey('servidores.id'), nullable=True)
