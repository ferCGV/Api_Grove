from passlib.context import CryptContext

pdw_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def hash_password (password):
    return pdw_context.hash(password)

def verify_password(plain_password:str , hashed_password:str):
    return pdw_context.verify(plain_password,hashed_password)
    
