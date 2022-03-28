from os import system
import modulecrypt as CRYPT
import module_decrypt as DECRYPT

YELLOW = '\033[93m'
OK = '\033[92m' #VERT
FAIL = '\033[91m'  # RED
RESET = '\033[0m'

while(True):

    menu = input(YELLOW + "\n\nSi tu veux Crypter un mot tape 1\nSi tu veux décrypter un mot tape 2\nSi tu veux en finir tape 3\n" + RESET)
    

    if menu == "1":
        system('clear')
        text = input("Quel mot veux tu crypter: ")
        nb = int(input("De combien veux tu décaler: "))
        print(OK + "Voila ton mot crypté :", CRYPT.crypt(text,nb) + RESET)

    elif menu == "2":
        os.system("clear")
        text = input("Quel mot veux tu décrypter: ")
        nb = int(input("Quel est le décalage: "))
        print(OK + "Voila ton mot décrypté: ", DECRYPT.decrypt(text, nb) + RESET)

    elif menu == "3":
        break

    else:
        os.system("clear")
        print(FAIL + "\nMerci de taper 1,2 ou 3" + RESET)
    



