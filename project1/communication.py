from decode import decoder
from encode import encoder

assert decoder(encoder("alodicksiano", 3450, 3, 100)) == "alodicksiano"
assert decoder(encoder("alodicksiano", 1420, 145, 100)) == "alodicksiano"
assert decoder(encoder("alodicksiano", 9540, 342, 2540)) == "alodicksiano"
assert decoder(encoder("123456789 123456789 123456789 123456789", 5402, 45, 50)) == "123456789 123456789 123456789 123456789"
