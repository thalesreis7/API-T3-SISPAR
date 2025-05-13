from flask import request, jsonify
from src.model import db
from src.model.reembolso_model import Reembolso

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')

@bp_reembolso.route('/visualizar-todos-reembolsos')
def visualizar_todos_reembolsos():
    reembolsos = db.session.execute(
        db.select(Reembolso)
    ).scalars().all()

    reembolsos = [reembolso.all_data() for colaborador in reembolsos]
    
    return reembolsos


@bp_reembolso.route('/solicitar-reembolso', methods=['POST'])
def solicitar_reembolso():
    dados_requisicao = request.get_json()
    
    novo_reembolso = Reembolso(
        id_colaborador=dados_requisicao['id_colaborador'],
        valor=dados_requisicao['valor'],
        descricao=dados_requisicao['descricao']
    )
    
    db.session.add(novo_reembolso)
    db.session.commit()
    
    return jsonify({'mensagem': 'Reembolso solicitado com sucesso'}), 201
