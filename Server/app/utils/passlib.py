
from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

def hashPassword(passw):
    return context.hash(passw)

def verifyPassword(passw , hashed):
    return context.verify(passw , hashed)