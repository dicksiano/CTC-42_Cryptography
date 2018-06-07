import Crypto # pip install rsa for Python2
from Crypto import Random
from Crypto.PublicKey import RSA
import ast
import hashlib

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

# Alice encrypts the message and sends the message and its hash to Bob
text = 'Dicksiano'
hash_text = hashlib.sha512(text).hexdigest()
print("SHA512: ")
print(hash_text)
print

# https://www.dlitz.net/software/pycrypto/doc/#crypto-publickey-public-key-algorithms
encrypted = key.publickey().encrypt(text, 32)

print('encrypted: ')
print(encrypted)
print

decrypted = key.decrypt(ast.literal_eval( str(encrypted)) )
print('decrypted: ')
print(decrypted)
