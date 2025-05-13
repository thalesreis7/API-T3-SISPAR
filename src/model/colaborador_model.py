from src.model import db # traz a instancia do sql alchemy para o arquivo

from sqlalchemy.schema import Column # Traz o recurso para o ORM entender que o atributo sera uma coluna na tabela

from sqlalchemy.types import String, DECIMAL, Integer # Importa os tipos de dados que as colunas vão aceitar

class Colaborador(db.Model):
     
#---------------------------------------ATRIBUTOS--------------------------------------------------------------------
    # AQUI seria a mesma coisa que no banco de dados onde temos: nome VARCHAR(100)
    # AQUI  no id seria o que temos no banco de dados: id INT AUT0_INCREMENT PRIMARY KEY
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(50))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))

#--------------------------------------------------------------------------------------------------------------------
    # self é a mesma coisa que o this no JS que faz referencia ao atributo da classe
    def __init__(self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
        
    # -------------------------------------------------------------
        def to_dict(self) -> dict:
            return {
                'email': self.email,
                'senha': self.senha,
            }
    
        def all_data(self) -> dict:
            return {
               'id': self.id,
               'nome': self.nome,
               'cargo': self.cargo,
               'salario': self.salario,
               'email': self.email
            }