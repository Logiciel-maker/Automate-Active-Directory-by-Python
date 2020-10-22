import argparse
import datetime
import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess

date_time = datetime.datetime.now()

""""
Cette classe implemente le service offert par le serveur
""""
class MonitorService(rpyc.Service):
    """
    Est exécuté à chaque fois qu'il y'a un client se connecte au serveur
    """
    def on_connect(self, connection):
        print('\nConnected on {}'.format(date_time))
    """
    Est exécuté à chaque fois qu'un client se deconnecte au serveur
    """
    def on_disconnect(self, connection):
        print('Disconnected on {}\n'.format(date_time))
    """
    Permet au client d'exécuter une commande sur l'active directory,
    run_command(command), sera la fonction appelé par le client connecté.
    Ainsi le serveur active directory exécute la commande => command
    """
    def exposed_run_command(self, command):
        try:
            #crée un processus(programme d'exécution) éxécutant la commande
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as Error:
            print(Error.returncode)
            print(Error.output)
""""
Fonction exécuté par le serveur
""""
def main():

    parser = argparse.ArgumentParser(description='Active Directory BOT')
    ##Recupère un numero de port pour ouvrir une écoute active
    parser.add_argument('-port', type=int, help="Enter custom port number")
    args = parser.parse_args()
    port = args.port
    if not port:
        port = 19961
    ##rend le service public, aux client connecté
    #création d'un processus qui va attendre la connection d'un client, et ensuite 
    # lui offrir les services exposé par la classe MonitorService
    t = ThreadedServer(MonitorService, port=port)
    #lance le serveur
    t.start()


if __name__ == "__main__":
    main()
