# Armazena as configurações do ambiente de desenvolvimento
from os import environ # Esse arquivo tem acesso as variaveis de ambiente
from dotenv import load_dotenv # Carregamento das variaveis de ambiente nesse arquivo

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_DEV') # Puxa a variavel de ambiente e utiliza a conexão
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Otimiza as Querys no banco de dados