from flask import Flask, escape, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'App Flask containerizado com sucesso!'

@app.route('/users/')
@app.route('/users/<username>')
def show_username(username=None):
    if username == None:
        return 'Lista de usuários'
    return f'Nome do usuário é {escape(username)}.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')

# BUILD DOCKER IMAGE: docker build . -t flask-webapp
# RUN DOCKER CONTAINER : docker run --rm -p 8000:8000 flask-webapp
