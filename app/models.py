import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Chaves(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(255), nullable=False)
  situacao = db.Column(db.String(255), nullable=False)
  status = db.Column(db.String(255), default='disponivel')


class Servidores(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(255), nullable=False)
  cpf = db.Column(db.String(255), unique=True, nullable=False)
  contato = db.Column(db.String(255))
  nascimento = db.Column(db.TIMESTAMP)
  status = db.Column(db.String(255), default='ativo')


class Emprestimos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  datahora_emprestimo = db.Column(db.TIMESTAMP, default=datetime.datetime.now())
  datahora_devolucao = db.Column(db.TIMESTAMP)
  status = db.Column(db.String(255), default='pendente')
  chave_id = db.Column(db.Integer, db.ForeignKey('chaves.id'))
  servidor_retirou_id = db.Column(db.Integer, db.ForeignKey('servidores.id'))
  servidor_devolveu_id = db.Column(db.Integer, db.ForeignKey('servidores.id'))