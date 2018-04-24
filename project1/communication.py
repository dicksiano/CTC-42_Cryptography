from decode import decoder
from encode import encoder

assert decoder(encoder("alodicksiano")) == "alodicksiano"
assert decoder(encoder("alodicksiano")) == "alodicksiano"
assert decoder(encoder("alodicksiano")) == "alodicksiano"
assert decoder(encoder("123456789 123456789 123456789 123456789")) == "123456789 123456789 123456789 123456789"
