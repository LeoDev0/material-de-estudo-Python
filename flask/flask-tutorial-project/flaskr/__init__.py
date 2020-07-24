import os
from flask import Flask


def create_app(test_config=None):
    # cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # carrega a instância config, se existente, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carrega o as configs dos testes se passarem
        app.config.from_mapping(test_config)

    # certifica que o diretório da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)

    return app

    # página simples para printar 'Hello, World!'
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    return app
