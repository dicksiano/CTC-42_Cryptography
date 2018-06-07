import random
import math
import fractions
from base64 import b64encode, b64decode
from collections import namedtuple

KeyPair = namedtuple('KeyPair', 'public private')
Key = namedtuple('Key', 'exponent modulus')

def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

# https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers
def is_prime(n, _precision_for_huge_n=16):
    if n == 1:
        return False
    if n in known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(try_composite(a, d, n, s) for a in known_primes[:_precision_for_huge_n])

known_primes = [2, 3]
known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

def random_prime(N=10**10):
    p = 1
    while not is_prime(p):
        p = random.randrange(N)
    return p

def mult_inverse(a, m) :     
    g = fractions.gcd(a, m)     
    if (g != 1):
        raise Exception("Inverse doesn't exist")         
    else:
        return mod_power(a, m - 2, m)
     
def mod_power(base, exp, mod) :     
    if mod == 1:
        return 0
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result 

assert mult_inverse(5, 7) == 3
assert mult_inverse(3, 7) == 5

def generate_key(N=10**10):
    p = random_prime(N)
    q = random_prime(N)

    while p == q:
        q = random_prime(N)

    n = p * q
    phi = (p-1) * (q-1) # Euler Function

    print(p)
    print(q)
    print(phi)

    private_key = random.randrange(phi)
    while fractions.gcd(private_key, phi) != 1:
        private_key = random.randrange(phi)

    public_key = mult_inverse(private_key, phi)

    return KeyPair(Key(public_key, n), Key(private_key, n))

def encode(msg, public_key):
    batch_size = int(math.log(public_key.modulus, 256))
    binary_msg = b64encode(msg.encode())
    result = []

    for start in range(0, len(binary_msg), batch_size):
        batch = binary_msg[start : start + batch_size]
        plain = 0

        print(batch)
        for byte in reversed(batch):
            print(byte)
            plain *= 2**8 # plain << 8
            plain += byte
        
        coded_batch = mod_power(plain, public_key.exponent, public_key.modulus)
        result.append(hex(coded_batch)[2:])
    return ":".join(result)
        

def decode(secret, private_key):
    result = []
    for batch in secret.split(":"):
        coded_batch = int(batch, 16)
        plain = mod_power(coded_batch, private_key.exponent, private_key.modulus)
        result.append(plain % 256)

        while plain > 0:
            plain = plain // 256
            result.append(plain % 256)
    
    print(bytes(result))
    return ( bytes(result ) ).decode()

if __name__ == '__main__':
    public_key, private_key = generate_key(10**10)
    msg = 'vai tomar no cu'

    secret = encode(msg, public_key)
    p = decode(secret, private_key)

    print('-' * 20)
    print(repr(msg))
    print(secret)
    print(repr(p))