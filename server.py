from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusDeviceContext, ModbusServerContext
from threading import Thread
import time

# Adresses Modbus
ADDR_BOUTON_PIETON = 0
ADDR_VOITURE = 1
ADDR_FEUX_VERT = 10
ADDR_FEUX_ROUGE = 11
ADDR_FEUX_ORANGE = 12
ADDR_FEUX_PIETON_VERT = 13
ADDR_FEUX_PIETON_ROUGE = 14

def feux(context, slave_id=0x00):
    """Gestionnaire des feux de circulation"""
    
    print("=== DÉMARRAGE DU SYSTÈME DE FEUX ===")
    
    # État initial
    context[slave_id].setValues(1, ADDR_FEUX_VERT, [1])  # Coils
    context[slave_id].setValues(1, ADDR_FEUX_PIETON_ROUGE, [1])  # Coils
    print(" État initial: Feu voiture VERT, Feu piéton ROUGE")
    
    while True:
        try:
            # Lecture des entrées - UTILISER COILS (0) au lieu de DISCRETE INPUTS (1)
            bouton = context[slave_id].getValues(1, ADDR_BOUTON_PIETON, count=1)[0]  # Coils
            voiture = context[slave_id].getValues(1, ADDR_VOITURE, count=1)[0]  # Coils
            
            # AFFICHAGE EN TEMPS RÉEL des entrées
            if bouton == 1:
                print(" BOUTON PIÉTON APPUYÉ - DÉTECTÉ PAR LE SERVEUR !")
            if voiture == 1:
                print(" VOITURE DÉTECTÉE - DÉTECTÉ PAR LE SERVEUR !")
            
            # Lecture des états actuels des feux pour le logging - COILS aussi
            feu_vert = context[slave_id].getValues(1, ADDR_FEUX_VERT, count=1)[0]
            feu_rouge = context[slave_id].getValues(1, ADDR_FEUX_ROUGE, count=1)[0]
            feu_orange = context[slave_id].getValues(1, ADDR_FEUX_ORANGE, count=1)[0]
            feu_pieton_vert = context[slave_id].getValues(1, ADDR_FEUX_PIETON_VERT, count=1)[0]
            feu_pieton_rouge = context[slave_id].getValues(1, ADDR_FEUX_PIETON_ROUGE, count=1)[0]
            
            # Affichage périodique de l'état (toutes les 10 secondes)
            if int(time.time()) % 10 == 0:
                print(f"État actuel - Bouton: {bouton}, Voiture: {voiture}")
                print(f" Feux - V:{feu_vert} O:{feu_orange} R:{feu_rouge} PV:{feu_pieton_vert} PR:{feu_pieton_rouge}")
            
            # Gestion bouton piéton
            if bouton == 1:
                print("=== DÉBUT SÉQUENCE PIÉTON ===")
                
                # Attente avant changement
                print("⏳ Attente de 3 secondes avant changement...")
                time.sleep(3)
                
                # Phase 1: Feu voiture orange - COILS
                context[slave_id].setValues(1, ADDR_FEUX_VERT, [0])
                context[slave_id].setValues(1, ADDR_FEUX_ORANGE, [1])
                print(" Feu voiture ORANGE")
                time.sleep(2)
                
                # Phase 2: Feu voiture rouge, piéton vert - COILS
                context[slave_id].setValues(1, ADDR_FEUX_ORANGE, [0])
                context[slave_id].setValues(1, ADDR_FEUX_ROUGE, [1])
                context[slave_id].setValues(1, ADDR_FEUX_PIETON_ROUGE, [0])
                context[slave_id].setValues(1, ADDR_FEUX_PIETON_VERT, [1])
                print(" Feu voiture ROUGE,  Feu piéton VERT")
                time.sleep(5)
                
                # Phase 3: Retour à l'état normal - COILS
                context[slave_id].setValues(1, ADDR_FEUX_ROUGE, [0])
                context[slave_id].setValues(1, ADDR_FEUX_PIETON_VERT, [0])
                context[slave_id].setValues(1, ADDR_FEUX_VERT, [1])
                context[slave_id].setValues(1, ADDR_FEUX_PIETON_ROUGE, [1])
                print(" Feu voiture VERT,  Feu piéton ROUGE")
                
                # Réinitialisation du bouton - COILS
                context[slave_id].setValues(1, ADDR_BOUTON_PIETON, [0])
                print("=== FIN SÉQUENCE PIÉTON ===")
            
            # Gestion détection voiture
            elif voiture == 1:
                print("=== DÉTECTION VOITURE ===")
                
                # Séquence orange rapide - COILS
                context[slave_id].setValues(1, ADDR_FEUX_VERT, [0])
                context[slave_id].setValues(1, ADDR_FEUX_ORANGE, [1])
                print(" Feu voiture ORANGE")
                time.sleep(2)
                
                context[slave_id].setValues(1, ADDR_FEUX_ORANGE, [0])
                context[slave_id].setValues(1, ADDR_FEUX_VERT, [1])
                print(" Feu voiture VERT")
                
                # Réinitialisation détection voiture - COILS
                context[slave_id].setValues(1, ADDR_VOITURE, [0])
                print("=== FIN SÉQUENCE VOITURE ===")
            
            time.sleep(0.5)  # Pause entre les vérifications
            
        except Exception as e:
            print(f" Erreur dans la boucle feux: {e}")
            time.sleep(1)

if __name__ == "__main__":
    # Initialisation des coils (tous à 0)
    initial_coils = [0] * 100
    
    device = ModbusDeviceContext(
        co=ModbusSequentialDataBlock(1, initial_coils)
    )
    context = ModbusServerContext(devices=device, single=True)

    # Démarrage du thread de gestion des feux
    feux_thread = Thread(target=feux, args=(context,))
    feux_thread.daemon = True
    feux_thread.start()

    print(" Serveur Modbus démarré sur 0.0.0.0:502")
    print(" En attente de commandes client...")
    print("Testez avec: python client.py")
    
    try:
        StartTcpServer(context=context, address=("0.0.0.0", 502))
    except KeyboardInterrupt:
        print("Serveur arrêté")