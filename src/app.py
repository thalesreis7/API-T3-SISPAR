# RESPONSÁVEL por construir nossa aplicação, cria a instância do Flask com as configs
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger

swagger_config = {
    "headers": [], # <-- Cabeçalhos HTTP a serem incluídos nos dados de resposta.
    "specs": [ # <-- Lista de especificações de documentação
       {
           "endpoint": "apispec", # Da um nome de referencia para a docmentação
           "route": "/apispec.json/", # Rota arquivo JSON para a construção da docmentação
           "rule_filter": lambda rule: True, # <-- Todas as rotas/endpoints serão documentadas
           "model_filter": lambda tag: True,
       } 
    ],
    "static_url_path": "/flasgger_static", # <-- Caminho para a pasta de arquivos estáticos, geralmente para arquivos CSS e JS
    "swagger_ui" : True, # <-- Habilita a interface de documentação Swagger
    "specs_route": "/apidocs/" # <-- Caminho para a documentação Swagger
}

def create_app():
    app = Flask(__name__) # Instancia a aplicação, __name__ é o nome do módulo ou pacote usado para inicializar o aplicativo.
    CORS(app, origins=["*"]) # <--- A política de CORS seja impementada em TODA aplicação
    app.register_blueprint(bp_colaborador)#Registra as blueprint colaborador
    app.register_blueprint(bp_reembolso)
    app.config.from_object(Config)# puxa toda a configuração dos nossos objetos
    db.init_app(app)# Inicia o conexão com o banco de dados
    
    Swagger(app, config=swagger_config)# chama as configs do Swagger, para documentar os JSON
    
    with app.app_context(): # Se as tabelas não existem, crie.
        db.create_all()# Cria as tabelas no banco de dados
    
    return app
