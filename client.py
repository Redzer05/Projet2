from pymodbus.client import ModbusTcpClient  # Importe la classe client Modbus TCP
import time  # Importe le module time pour les pauses

# Adresses Modbus à adapter selon ton automate
ADDR_BOUTON_PIETON = 0  # Adresse de l'entrée bouton piéton
ADDR_VOITURE = 1        # Adresse de l'entrée détection voiture
ADDR_FEUX_VERT = 10     # Adresse de la sortie feu vert
ADDR_FEUX_ROUGE = 11    # Adresse de la sortie feu rouge
ADDR_FEUX_ORANGE = 12   # Adresse de la sortie feu orange

client = ModbusTcpClient('127.0.0.1', port=502)  # Crée un client Modbus TCP connecté à localhost sur le port 502
client.connect()  # Établit la connexion avec le serveur Modbus

def changer_feux(vert=False, orange=False, rouge=True):
    client.write_coil(ADDR_FEUX_VERT, vert)    # Commande la sortie feu vert
    client.write_coil(ADDR_FEUX_ORANGE, orange)  # Commande la sortie feu orange
    client.write_coil(ADDR_FEUX_ROUGE, rouge)    # Commande la sortie feu rouge
    print(f"Feux - Vert: {vert}, Orange: {orange}, Rouge: {rouge}")  # Affiche l'état des feux

try:
    while True:  # Boucle infinie pour gérer les cycles du feu
        bouton_pieton = client.read_discrete_inputs(ADDR_BOUTON_PIETON, 1)  # Lit l'entrée bouton piéton
        voiture = client.read_discrete_inputs(ADDR_VOITURE, 1)  # Lit l'entrée détection voiture

        pieton = bouton_pieton.bits[0] if not bouton_pieton.isError() else False  # Récupère l'état du bouton piéton
        car = voiture.bits[0] if not voiture.isError() else False  # Récupère l'état de la détection voiture

        if pieton:  # Si un piéton est détecté
            print("Piéton détecté, adaptation du cycle...")
            changer_feux(vert=False, orange=False, rouge=True)  # Feu rouge pour sécuriser
            print("Attente pour sécuriser la traversée piétonne...")
            time.sleep(2)  # Pause de sécurité
            changer_feux(vert=True, orange=False, rouge=False)  # Feu vert (ici pour piéton, à adapter si besoin)
            print("Piéton traverse...")
            time.sleep(3)  # Temps de traversée
            changer_feux(vert=False, orange=True, rouge=False)  # Feu orange
            time.sleep(1)  # Pause orange
            changer_feux(vert=False, orange=False, rouge=True)  # Retour au rouge
        elif car:  # Si une voiture est détectée
            print("Véhicule détecté, adaptation du cycle...")
            changer_feux(vert=True, orange=False, rouge=False)  # Feu vert voiture
            time.sleep(4)  # Temps de passage voiture
            changer_feux(vert=False, orange=True, rouge=False)  # Feu orange
            time.sleep(2)  # Pause orange
            changer_feux(vert=False, orange=False, rouge=True)  # Retour au rouge
        else:  # Si rien n'est détecté
            print("Pas de trafic détecté, feu reste rouge.")
            changer_feux(vert=False, orange=False, rouge=True)  # Feu rouge
            time.sleep(3)  # Pause

        print("--- Nouveau cycle ---")
        time.sleep(0.5)  # Petite pause avant le prochain cycle

finally:
    client.close()  # Ferme la connexion Modbus proprement