
from decode import decoder
from encode import encoder

if __name__ == "__main__":
    input = open("inputText.txt", "r")
    text = input.read()

    criptedText = encoder(text, 3450, 3, 100)

    criptedFile = open("outputText.txt", "w")
    criptedFile.write(criptedText)
    criptedFile.close()

    decriptedText = decoder(criptedText)
    decriptedFile = open("finalText.txt", "w")
    decriptedFile.write(decriptedText)
    decriptedFile.close()
