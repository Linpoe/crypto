#text = input("Quel mot veux tu décrypter: ")
#nb = int(input("Quel est le décalage: "))

def decrypt (text,nb):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    KEY = ALPHABET[-nb:] + ALPHABET[0:-nb]
    text_decrypt = ""

    for i in text:
        if i.upper() in ALPHABET:
            text_decrypt = text_decrypt + KEY[ALPHABET.index(i.upper())]
        else:
            continue
    return text_decrypt

#print(decrypt (text,nb))