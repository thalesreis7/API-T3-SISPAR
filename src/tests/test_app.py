#para a bibli encontrar o arquivo teste, ele e tem que ser chamado como test
import pytest #traz a biblioteca de testes
import time # manipula o tempo
from src.model.colaborador_model import Colaborador
from src.app import create_app

#-------------------configs para teste-------------------
@pytest.fixture # indentificar funções de confgs para o test
def app():
    app = create_app()
    yield app # garda os valores em memoria
    
@pytest.fixture
def client(app):
    return app.test_client()
#--------------------------------------------------------
# as funções precisã´começar como test no nome
def test_desempenho_requisicao_get(client):
    comeco = time.time()# pega a hora atual e transforma em segundos
    
    for _ in range(100):
        resposta = client.get("/colaborador/todos-colaboradores")
    
    fim = time.time() - comeco
    assert fim < 0.2
