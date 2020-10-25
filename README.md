# Automate-Active-Directory-by-Python
Automate the creation and management of active directory user accounts.

Ce programme fait en trois parties  permet la création et la gestion des comptes utilisateurs active directory.

Adbot.py : Met le serveur en écoute, reçoit les commandes et les exécutes.

Adclient.py : Se connecte au serveur et envoie  les commandes à exécuter.

Manageclient.py : Teste l’ensemble des fonctions.

Utilisation:
Lancer le script managead.py avec l'option -test suivi de l'action que vous souhatez effectuer.

1 ... Opération de création d'un utilisateur.

Action: Lancer le script manage.py -test createuser, entrer le nom de l'utilisateur et valider, son id et valider, ensuite son nom complet et valider.

2...Opération de création de groupes

Action: Lancer le script manage.py -test creategroupe, et entrer le nom du groupe et valider.

3.....Opération de création d'un utilisation et son ajout dans un groupe.

Action: Lancer le script manage.py -test createuser, enter son nom et valider, ensuite  specifier le nom du groupe dans lequel vous souhaitez l'ajouter et valider. 

4...Operation de création d'utilisateurs multiples.

Action: Lancer le script manage.py -test multiplecreation, ensuite indiquer le nom du fichier csv qui contient les noms des utilisateurs et valider.

5...Operation changer le mot de passe de l'utilisateur.

Action: Lancer le script manage.py -test changepass, entrer le nom de l'utilisateur et valider, ensuite indiquer le nouveau mot de passe.

