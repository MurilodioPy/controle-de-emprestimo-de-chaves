import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-padrão'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://seu-usuario:sua-senha@localhost/seu-banco-de-dados'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento das modificações do SQLAlchemy

    # Configurações adicionais do aplicativo
    DEBUG = True  # Ative o modo de depuração (defina como False em produção)
    SQLALCHEMY_ECHO = False  # Ative o modo de eco (verbose) do SQLAlchemy (defina como False em produção)
