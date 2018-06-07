import Crypto # pip install rsa for Python2
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast
import hashlib

random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()


# Alice encrypts the message and sends the message and its hash to Bob
text = 'This is Alice msg'
hash_text = hashlib.sha512(text).hexdigest()
signature = private_key.sign(hash_text, 'Alice')
print("SHA512: ")
print(hash_text)
print

print("Signature: ")
print(signature)
print

# Check paramters: p, q, n
#print(private_key.p)
#print(private_key.q)
#print(private_key.n)

# https://www.dlitz.net/software/pycrypto/doc/#crypto-publickey-public-key-algorithms
encrypted = private_key.publickey().encrypt(text, 32)

print('encrypted: ')
print(encrypted)
print

if public_key.verify(hash_text, signature):
    print("Bob verifies that the message came from Alice!\n")

decrypted = private_key.decrypt(ast.literal_eval( str(encrypted)) )
print('decrypted: ')
print(decrypted)



    """signer = PKCS1_v1_5.new(key)
    digest = SHA512.new()
    digest.update(message)
    return signer.verify(digest, signature)"""


    """signer = PKCS1_v1_5.new(key)
    digest = SHA512.new()
    digest.update(message)
    return signer.sign(digest)"""