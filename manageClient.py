import adClient #Importer toutes les fonctions se trouvant dans le fichier adClient
import csv

"""
Classe permettant de tester l'ensemble des fonctions
"""
class Test:
    # initialise les attributs de la classes.
    # ici users est un attribu de la classe Test
    def __init__(self):
        self.users = [] #un tableau vide
    def getUsers(self):
        return self.users
    
    """
    Lis tous les utlisateurs se trouvant dans le fichier csvFile (utilisateurs.csv)
    les ajoutes dans le tableau users
    """
    def retrieveUsersFromCSV(self,csvFile):
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
                self.users.append(user) # ajoute l'utilisateur courant dans le tableau users
    """
    Test la création d'un utilisateur
    """
    def createUser(self,user):
        print("Creation de l'utilisateur : ID: {} , NOM :{} , Nom officiel : {}".format(user["id"],user["name"],user["officialName"]))
        adClient.create_user(user["name"],user["id"],user["officialName"])
        print("utilisateur crée.")
    def updateUserPassword(self,user,newPass):
        adClient.user_password_change(user["name"],newPass)
        print("Modification du mot de passe avec succès")
    
    """
    Test la création d'un group
    """
    def createGroup(self, groupName):
        print("Creation du grouupe Nom du Goupe:{}".format(groupName))
        adClient.ad_group(groupName,"add")
        print("Groupe créé")
    
    """
    Test la supression d'un utiliateur
    """
    def removeUser(self,user):
        adClient.manage_user(user["name"],"delete")
        print("L'utilisateur {} a été supprimé".format(user["name"]))
    """
    les utilisateus dans users doivent être créé au préalable
    """
    def addUsersInGroup(self,users,groupName):
        
        for user in self.users:
            adClient.group_user(groupName,"add",user["name"])
        print("{} utilisateurs ont été ajouté dans le groupe {}".format(len(users),groupName))

    def removeGroup(self,groupName):
        adClient.ad_group(groupName,"remove")
        print("Le groupe {} a été supprimé".format(groupName))
    """
    crée tous les utilisateurs se trouvant dans le tableau users
    """
    def createAllUsers(self):
        for user in self.users:
            self.createUser(user)
    """
    supprime tous les utilisateurs se trouvantd ans le tableau users
    """
    def removeAllUsers(self):
        for user in self.users:
            self.removeUser(user)
    def executeTest(self,numeroTest):
        groupes = ["DevOps","Ressources Humaines"]
        users = self.getUsers() #recupération des utlisateurs dans le tableau users
        if(numeroTest==1):
            userOne = self.users[0]
            #Test Numero 1
            #crée un utilisateur n°1
            self.createUser(userOne)
            #change le mot de passe de l'utilisatuer n°1
            #self.updateUserPassword(userOne,"nouveauMotDePasse123")
            #supprime l'utlisateur n°1
            #self.removeUser(userOne)  
            None     
        elif numeroTest==2:
            #Test Numero 2
            #crée deux  groupes "DevOps" "Ressources Humaines"
            #self.createGroup(groupes[0])
            #self.createGroup(groupes[1])
            #self.createUser(users[0])
            #self.createUser(users[1])
            #self.addUsersInGroup(users[1:3],'DevOps') # ajoute dans le groupe DevOps les trois premiers utlisateurs
            
            #self.removeGroup('DevOps')
            #self.removeGroup('Ressources Humaines')
            #self.removeUser(users[0])       
            #self.removeUser(users[1])       
            None
        elif numeroTest==3:
            #Test numero 3, création multiple
            #crée tous les utlisateurs se trouvant dans le fichier csv
            #self.createAllUsers()

            #self.createGroup(groupes[0])
            #self.createGroup(groupes[1])
            #Ajoute la première moitié des utilisateurs dans le groupe DevOps
            #middle =int( len(users)/2)
            #self.addUsersInGroup(users[:middle],"DevOps")
            #Ajoute la deuxième moitié des utilisateurs dans le groupe Ressources Humaines
            #self.addUsersInGroup(users[middle:],"Ressources Humaines")

            #Supprimer les deux groupes
            #self.removeGroup(groupes[0])
            #self.removeGroup(groupes[1])
            #supprimer tous les utilisateurs 
            #self.removeAllUsers()
            None
def main():
    test = Test() # crée une instance de test (crée un objet)
    test.retrieveUsersFromCSV('utlisateurs.csv') #lecture de tous les utlisateurs 
    test.executeTest(1)
    #test.executeTest(2)
    #test.executeTest(3)
main()