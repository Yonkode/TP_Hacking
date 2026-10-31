import os.path
import subprocess
import sys
import random
import string
import bcrypt

def checkExistence():
    if os.path.exists("vault.txt"):
        pass
    else:
        file = open("vault.txt", "w")
        file.close()

def hashPassword(password):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash

def appenNewPassword():
    with open("vault.txt", "a") as appender:
        print()
        username = input("Veuiller enterr un nom d'utilisateur : " )
        password = input("Veuillez enter le mot de passe : ")
        website = input("Veuiller entrer l'adresse du site web : ")
        print()

        hashedPassword = hashPassword(password)

        usernameline = "Nom d'utilisateur : " + username + "\n"
        passworline = "Mot de passe : " + str(hashedPassword) + "\n"
        websiteline = "Site web : " + website + "\n"

        appender.write("-"* 60 +"\n")
        appender.write(usernameline)
        appender.write(passworline)
        appender.write(websiteline)
        appender.write("-"*60)




def readPassword():
    content = ''
    with open("vault.txt", "r") as reader:
        content = reader.read()
        print()
        print(content)


def generateNewPassword(PasswordLength):
    randomString = string.ascii_letters + string.digits + string.punctuation
    newPassword = ''
    for i in range(int(PasswordLength)):
        newPassword+= random.choice(randomString)
    print()
    print("Voici votre mot de passe : " + newPassword)


subprocess.call("clear", shell = True)

print('-'*60)
print("Bienvrnur dans le gestionnaire de mots de passe! ")
print('-'*60)

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