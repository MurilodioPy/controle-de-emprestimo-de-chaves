from app import app

@app.route('/')
def index():
    return "<h1>Controle de empréstimo de chaves</h1>"

@app.route('/about')
def sobre():
    return "<h1>Sobre o sistema</h1>"

@app.route('/usuarios')
def users():
    return "<h1>Usuários</h1>"

@app.route('/chaves')
def chave():
    return "<h1>Chaves</h1>"