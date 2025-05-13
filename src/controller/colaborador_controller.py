# É uma rota e também determina uma rota, isola elas e junta os endpoints.
# request ->  recurso do FLASK trabalha com as  requisições, pega o conteúdo da requisição
# jsonify -> trabalha com as respostas -> enviando dados no formato JSON convertendo para JSON e envia um status code: 200 e por ai vai

from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')

@bp_colaborador.route('/todos-colaboradores')
def pegar_dados_todos_colaboradores():
    
    colaboradores = db.session.execute(
        db.select(Colaborador)
    ).scalars().all()
    
    #execute essa expressão para cada item do iterável
    colaboradores = [colaborador.all_data() for colaborador in colaboradores]
    
    return colaboradores
#POST ENVIA DADOS 
@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from('../docs/Colaborador/cadastrar_colaborador.yml')
def cadastrar_novo_colaborador():
    
    dados_requisição = request.get_json()
   
    novo_colaborador = Colaborador(
        nome=dados_requisição['nome'], # Pegue no json o valor relacionado a chave nome e assim por diante
        email=dados_requisição['email'],
        senha=hash_senha(dados_requisição['senha']),
        cargo=dados_requisição['cargo'],
        salario=dados_requisição['salario']
    )
    
    # Seria a mesma coisa no banco de dados: INSERT INTO tb_colaborador(nome, email, senha, cargo, salario) VALUES (VALOR1, VALOR2, VALOR3 VALOR4, VALOR5)
    db.session.add(novo_colaborador)
    db.session.commit() # Essa linha executa a query
    
    # envia uma mensagem entre chaves e o status code de 201 que é o status de created no banco de  dados.
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'}), 201

# endereço/colaborador/atualizar/ e o id 
# onde tem <> sinaliza que os dados após o atualizar são dinâmicos, podendo ser de qualquer id
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atulaizar_dados_colaborador(id_colaborador):
    dados_requisicao = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']
    return jsonify({'mensagem': "Dados do colaborador atualizado com sucesso!!" }), 200
    
    
@bp_colaborador.route('/login', methods=['POST'])
def login():
    dados_requisicao = request.get_json()
        
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os dados precisam ser preenchidos'}), 400
    
    #select * from  [TABELA] NO banco de dados
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.email == email)
    ).scalar() # traz a linha de informação  ou None, se for igual a none n
    
    if not colaborador:
        return jsonify({'mensagem': 'Usuario não encontrado'}),404
    
    colaborador = colaborador.to_dict()
    
    if email == colaborador.get('email') and checar_senha(senha,colaborador.get('senha')):
        return jsonify({'mesagem': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'mensagem': 'Credenciais inválidas!'}),400
    
    