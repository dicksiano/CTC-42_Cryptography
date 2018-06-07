import my_rsa

plain_text = "CTC 42 - Criptografia"

raw_input()
print("Alice send her public Key on the channel!\n")
private_key_alice, public_key_alice = my_rsa.generateKeys()

raw_input()
print("Bob send his public Key on the channel!\n")
private_key_bob, public_key_bob = my_rsa.generateKeys()

# First of all, Alice will:
#   i. encrypt the plain_text
#  ii. sign the message
# iii. send the message to Bob

    # Encrypt with Receptor's public key
    # In that case, only the desired Receptor is able to decrypt the message
encrypted_text = my_rsa.encrypt(plain_text, public_key_bob)

raw_input()
print("Alice encrypted the plain text!\n")

    # Sign with Sender's private key
    # In that case, only the Sender could send the message
digital_signature = my_rsa.sign(plain_text, private_key_alice)

raw_input()
print("Alice generated the digital signature!\n")

raw_input()
print("Alice sent the encrypted message and the digital signature!\n")

# After that, Bob will:
#   i. Receive the message
#  ii. Decrypt the message
# iii. Verify if the signature is valid

raw_input()
print("Bob received the message!\n")

    # Decrypt with Receptor's private keys
decrypted_text = my_rsa.decrypt(encrypted_text, private_key_bob)

raw_input()
print("Bob decrypted the secret!\n")

    # Check if the signature is valid
is_valid = my_rsa.verify(decrypted_text, digital_signature, private_key_alice)

raw_input()
print("Bob evaluate the digital signature!\n")

raw_input()
print("...\n")
raw_input()
print("...\n")
raw_input()
print("...\n")

if is_valid:
    print("The digtal signature is valid!")
    print("Decrypted message: ")
    print(decrypted_text)
    print
else:
    print("DANGER! The digital signature is not valid!\n")