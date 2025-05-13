from flask_bcrypt import bcrypt

#criptografa as senhas
def hash_senha(senha):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode('utf-8'), salt)

#desincriptografa as senhas para checar 
def checar_senha(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))