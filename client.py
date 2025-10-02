
from pymodbus.client import ModbusTcpClient
import time # Importe le module time pour les pauses
ADDR_BOUTON_PIETON = 0  # Adresse de l'entrée bouton piéton
ADDR_VOITURE = 1        # Adresse de l'entrée détection voiture


# Connexion au serveur Modbus


def bouton_pieton_appuye():
    client = ModbusTcpClient('127.0.0.1', port=502)
    client.connect()
    """Simule l'appui sur le bouton piéton en écrivant 1 à l'adresse du bouton piéton."""
    client.write_register(ADDR_BOUTON_PIETON, value=1)
    print("Bouton piéton appuyé.")
    client.close()

def voiture_detectee():
    client = ModbusTcpClient('127.0.0.1', port=502)
    client.connect()
    """Simule la détection d'une voiture en écrivant 1 à l'adresse de détection voiture."""
    client.write_coils(ADDR_VOITURE, value=1)  
    print("Voiture détectée.")      
    client.close()

bouton_pieton_appuye()  # Simule l'appui sur le bouton piéton


# client.close()  # Ferme la connexion Modbus proprement (déjà fermé dans la fonction)