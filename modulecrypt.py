#text = input("Quel mot veux tu crypter: ")
#nb = int(input("De combien veux tu décaler: "))

def crypt (text,nb):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    KEY = ALPHABET[nb:] + ALPHABET[0:nb]
    text_crypt = ""

    for i in text:
        if i.upper() in ALPHABET:
            text_crypt = text_crypt + KEY[ALPHABET.index(i.upper())]
        else:
            continue
    return text_crypt
#print (crypt (text,nb))