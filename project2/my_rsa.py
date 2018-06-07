import Crypto # pip install rsa for Python2

# Dependencies
from Crypto import Random
from Crypto.PublicKey import RSA
import hashlib
import ast
from base64 import b64encode, b64decode

def sign(message, key):
    hash_text = hashlib.sha512(message).hexdigest()
    signature = encrypt(hash_text, key)

    return signature

def verify(message, signature, key):
    hash_text = hashlib.sha512(message).hexdigest()
    decrypted_sign = decrypt(signature, key )

    return hash_text == decrypted_sign

def generateKeys():
    private_key = RSA.generate(1024, Random.new().read)
    return private_key, private_key.publickey()

def encrypt(plain_text, key):
    return key.encrypt(plain_text, 32)

def decrypt(secret, key):
    return key.decrypt(ast.literal_eval(str(secret)))