# from app import app
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8080,use_reloader=False)
