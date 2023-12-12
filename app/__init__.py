from flask import Flask, render_template
import os
from . database import db
from app.views.chave import chave_bp
from app.views.servidor import servidor_bp
from app.views.emprestimo import emprestimo_bp
from app.views.aplicativo import aplicativo_bp


def create_app():
    app = Flask(__name__)
    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error/404.html'), 404
    # ?unix_socket=/var/run/mysqld/mysqld.sock
    # 'mysql://pjflask:Pjflask1@localhost/pjflask'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pjflask:Pjflask1@mysql:3306/pjflask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.secret_key = ''
    app.secret_key = os.urandom(24)
    app.secret_key = os.environ.get('SECRET_KEY', 'dev')

    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except Exception as exception:
            print("Error: db.create_all() in __init__.py: " + str(exception))
        finally:
            print("db.create_all() in __init__.py was successful")
    
    app.register_blueprint(aplicativo_bp, url_prefix='/')
    app.register_blueprint(chave_bp, url_prefix='/chave')
    app.register_blueprint(servidor_bp, url_prefix='/servidor')
    app.register_blueprint(emprestimo_bp, url_prefix='/emprestimo')

    return app