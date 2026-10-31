import os.path
import subprocess
import sys
import random
import string
import cryptography.fernet
import stdiomask

def generateMasterPassword():
    key = cryptography.fernet.Fernet.generate_key()
    with open("./master.key", "wb") as masterPasswordWriter:
        masterPasswordWriter.write(key)


def loadMasterPassword():
    return open("./master.key", "rb").read()


def createVault():
    vault = open("./vault.txt", "wb")
    vault.close()


def encryptData(data):
    f = cryptography.fernet.Fernet(loadMasterPassword())
    with open("./vault.txt", "rb") as vaultReader:
        encryptedData = vaultReader.read()

    if encryptedData.decode() == '':
        return f.encrypt(data.encode())
    else:
        decrypteData = f.decrypt(encryptedData)
        newData = decrypteData.decode() + data
        return f.encrypt(newData.encode())


def decryptedData(encryptedData):
    f = cryptography.fernet.Fernet(loadMasterPassword())
    return f.decrypt(encryptedData)


def appenNewPassword():
    print()
    userName = input("Veuiller entrer un nom d'utilisateur : " )
    password = stdiomask.getpass(prompt="Veuillez entrer le mot de passe : ", mask = '*')
    website = input("Veuiller entrer l'adresse du site web : ")
    print()

    userNameline = "Nom d'utilisateur : " + userName + "\n"
    passwordLine = "Mot de passe : " + password + "\n"
    websiteLine = "Site web : " + website + "\n\n"

    encryptedData = encryptData(userNameline + passwordLine + websiteLine)

    with open("./vault.txt", "wb") as vaultWriter:
        vaultWriter.write(encryptedData)


def readPassword():
    with open("./vault.txt", "rb") as passwordsReader:
        encryptedData = passwordsReader.read()
        print()
        print(decryptedData(encryptedData).decode())


def generateNewPassword(PasswordLength):
    randomString = string.ascii_letters + string.digits + string.punctuation
    newPassword = ''
    for i in range(int(PasswordLength)):
        newPassword+= random.choice(randomString)
    print()
    print("Voici votre mot de passe : " + newPassword)


subprocess.call("clear", shell = True)

print('-'*60)
print("Bienvenue dans le gestionnaire de mots de passe! ")
print('-'*60)

if os.path.exists("./vault.txt") and os.path.exists("./master.key"):
    print("Vous pouvez selectionner l'une des options suivantes : ")
    print("""
    1- Sauvegarder un nouveau mot de passe
    2- Generer un nouveau mot de passe aleatoire
    3- Obtenir la liste de vos mots de passe
    """)

    userChoice = input("Que souhaitez-vous faire? (1/2/3)")

    if userChoice == "1":
        appenNewPassword()
    elif userChoice == "2":
        passwordLength = input("Quelle est la longueu rsouhaitee pour le mot de passe?")
        if not string.ascii_letters in passwordLength:
            generateNewPassword(int(passwordLength))
        else:
            print("Merci de renter un nombre la prochaine fois...")
            sys.exit()
    elif userChoice == "3":
        readPassword()
    else:
        print("L'option selectionne n'existe pas...")
        sys.exit()

else:
    print("Generation d'un mot de passe maitre et d'un coffre de mots de passe...")
    generateMasterPassword()
    createVault()
    print("Generation terminer veuiller relancer le programme")