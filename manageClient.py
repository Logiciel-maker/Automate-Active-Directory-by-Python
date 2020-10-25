import adClient #Importer toutes les fonctions se trouvant dans le fichier adClient
import csv
import argparse


#créer un dictionnaire contenants les utilsateurs se trouvant dans le fichier csvFile

def retrieveUsersFromCSV(csvFile):
    users=[]
    try:
        with open(csvFile, mode='r') as csv_file: #Ouverture de fichier en mode lecture
            csv_reader = csv.DictReader(csv_file) #Lecture du fichier
            for row in csv_reader: #Parcour le fichier ligne par ligne
                username = row['username']
                employee_id = row['employee_id']
                official_name = row['official_name']
                #Crée un dictionniare pour faciliter la manipulation de l'objet
                user ={
                    "name":username,
                    "id":employee_id,
                    "officialName":official_name
                }
                users.append(user) # ajoute l'utilisateur courant dans le tableau users
    except FileNotFoundError:
        print("{} introuvable".format(csvFile))
    return users

def main():
    parser = argparse.ArgumentParser(description='Active Directory BOT')
    parser.add_argument('-test', type=str, help="Entrer le numero de test")
    args = parser.parse_args()
    testName = args.test
    if testName == 'createuser':
        username = input("Entrer le nom de l'utilisateur à créer : ")
        userId = input("Entrer l'identifiant de l'utilisateur : ")
        userOfficialName = input("Entrer le nom Official de l'utlisateur: ")
        user = {
            "name":username,
            "id":userId,
            "officialName":userOfficialName
        }
        #test createuser process
        print("Creation de l'utilisateur : ID: {} , NOM :{} , Nom officiel : {}".format(user["id"],user["name"],user["officialName"]))
        adClient.create_user(user["name"],user["id"],user["officialName"])
        print("utilisateur crée.")
        return
    elif testName=="changepass":
        username = input("Enter le nom de l'utlisateur : ")
        newpass = input("Entrer le nouveau mot de pass : ")
        adClient.user_password_change(username,newpass)
        print("modification du mot de passe avec succèss")
        return
    elif(testName=="deleteuser"):
        username= input("Entrer le nom de l'utilisateur a supprimer :")
        adClient.manage_user(username,'delete')
        print("L'utilisateur {} a été supprimé".format(username))
        return
    elif(testName=="creategroupe"):
        groupName= input("Enter le nom du groupe a créer :")
        print("Creation du grouupe Nom du Goupe:{}".format(groupName))
        adClient.ad_group(groupName,"add")
        print("Groupe créé")
        return
    elif(testName=="deletegroupe"):
        groupName = input("Entrer le nom du groupe a supprimer : ")
        adClient.ad_group(groupName,"remove")
        print("Le groupe {} a été supprimé".format(groupName))
        return 
    elif(testName=="adduser"):
        userName = input("Enter le nom de l'utilisateur :")
        groupName = input("Entrer le nom du groupe : ")
        adClient.group_user(groupName,"add",userName)
        print("{} a été ajouté dans le groupe {}".format(userName,groupName))
        return
    elif testName=="removeuser":
        userName = input("Enter le nom de l'utilisateur :")
        groupName = input("Entrer le nom du groupe : ")
        adClient.group_user(groupName,"remove",userName)
        print("{} a été supprimé du groupe {}".format(userName,groupName))
    elif testName =="multiplecreation":
        fileName = input("Enter le nom du ficher (format .csv):")
        try:
            users = retrieveUsersFromCSV(fileName)
            for user in users:
                print("Creation de l'utilisateur : ID: {} , NOM :{} , Nom officiel : {}".format(user["id"],user["name"],user["officialName"]))
                adClient.create_user(user["name"],user["id"],user["officialName"])
            return
        except FileExistsError:
            print("{} introuvable".format(fileName)) 
            return
    elif testName == "multiplesuppression":
        fileName = input("Enter le nom du ficher (format .csv):")
        users = retrieveUsersFromCSV(fileName)
        for user in users:
            adClient.manage_user(user["name"],'delete')
            print("L'utilisateur {} a été supprimé".format(user["name"]))
        return 
main()
