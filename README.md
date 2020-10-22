# Automate-Active-Directory-by-Python
Automate the creation and management of active directory user accounts.

Ce programme fait en trois parties  permet la création et la gestion des comptes utilisateurs active directory.

Adbot.py : Met le serveur en écoute, reçoit les commandes et les exécutes.

Adclient.py : Se connecte au serveur et envoie  les commandes à exécuter.

Manageclient.py : Test l’ensemble des fonctions.

Utilisation:
Le script adclient.py contient les différentes opérations que l'on peut effectuer.

1 ... Opération de création, suppression et de modification de mot de passe.
Action: Dans la fonction executeTest  décommenter  l'instruction que vous souhaitez effectuer et dans la fonction main decommanté test1.
En fonction des instructions décommenté on pourra donc créer, supprimer, changer le mot de passe d'un utilisateur.

2...Opération de création et de suppression de groupes
Action: Dans la fonction executeTest  décommenter l'instruction que vous souhaitez effectuer et dans la fonction main decommanté test2.
En fonction de chaque instruction décommentée on pourra créer des groupes, des utilisateurs, ajouter des utilisateurs dans des groupes.

3...Operation de création d'utilisateurs multiples
Action: Dans la fonction executeTest  décommenter l'instruction que vous souhaitez effectuer et dans la fonction main décommanté test3.
En fonction de chaque instruction décommentée on pourra créer plusieurs utilisateurs active directory à partir du fichier CSV.
On pourra aussi créer des groupes, supprimer, ajouter des utilisateurs de façon simultané dans des groupes.

