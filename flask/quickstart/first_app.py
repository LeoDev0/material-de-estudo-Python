from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {escape(name)}!'

""" 
* 'env FLASK_APP=first_app.py flask run' inicia a aplicação 

* É possível tbm especificar ip local do host '--host=127.0.0.1'
  e porta com '--port=8000'

===============================================================

* Outra forma de iniciar a aplicação seria usar esse trecho de 
código abaixo:

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

* e apenas rodar 'python first-app.py'

"""
