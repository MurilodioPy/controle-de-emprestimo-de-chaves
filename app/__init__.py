from flask import Flask
from . database import db
from app.views.chave import chave_bp
# from app.views.servidor import servidor_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pjflask:Pjflask1@localhost/pjflask?unix_socket=/var/run/mysqld/mysqld.sock'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    
    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
        except Exception as exception:
            print("Error: db.create_all() in __init__.py: " + str(exception))
        finally:
            print("db.create_all() in __init__.py was successful")
    
    app.register_blueprint(chave_bp, url_prefix='/')
    # app.register_blueprint(servidor_bp, url_prefix='/servidor')

    return app