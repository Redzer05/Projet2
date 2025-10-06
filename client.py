from pymodbus.client import ModbusTcpClient
import time
import random

ADDR_BOUTON_PIETON = 0
ADDR_VOITURE = 1

def bouton_pieton_appuye():
    client = ModbusTcpClient('127.0.0.1', port=502)
    try:
        if client.connect():
            result = client.write_coil(ADDR_BOUTON_PIETON, True)
            if not result.isError():
                print("✅ Bouton piéton appuyé - signal envoyé avec succès")
            else:
                print("❌ Erreur lors de l'envoi du signal bouton piéton")
        else:
            print("❌ Erreur de connexion au serveur")
    except Exception as e:
        print(f"❌ Exception: {e}")
    finally:
        client.close()

def voiture_detectee():
    client = ModbusTcpClient('127.0.0.1', port=502)
    try:
        if client.connect():
            result = client.write_coil(ADDR_VOITURE, True)
            if not result.isError():
                print("🚗 Voiture détectée - signal envoyé avec succès")
            else:
                print("❌ Erreur lors de l'envoi du signal voiture")
        else:
            print("❌ Erreur de connexion au serveur")
    except Exception as e:
        print(f"❌ Exception: {e}")
    finally:
        client.close()

def simulation_trafic():
    """Simule un trafic aléatoire avec bouton piéton et voitures"""
    print("=== DÉMARRAGE DE LA SIMULATION DE TRAFIC ===")
    
    while True:
        try:
            print("\n" + "="*50)
            print("Options disponibles:")
            print("1. Appuyer sur le bouton piéton")
            print("2. Quitter")
            print("3. Attendre une action aléatoire")
            
            choix = input("\nVotre choix (1/2/3): ").strip()
            
            if choix == "1":
                # Appui sur le bouton piéton
                bouton_pieton_appuye()
                
                # Décision aléatoire pour une voiture après l'appui piéton
                if random.random() < 0.6:  # 60% de chance qu'une voiture arrive
                    delai_voiture = random.uniform(2.0, 8.0)
                    print(f"⏰ Une voiture arrivera dans {delai_voiture:.1f} secondes...")
                    time.sleep(delai_voiture)
                    voiture_detectee()
                else:
                    print("🔕 Aucune voiture détectée après l'appui piéton")
                    
            elif choix == "2":
                print("👋 Arrêt de la simulation")
                break
                
            elif choix == "3":
                # Action complètement aléatoire
                if random.random() < 0.3:  # 30% de chance d'appui piéton
                    print("🎲 Action aléatoire: bouton piéton")
                    bouton_pieton_appuye()
                    
                    # Possibilité de voiture après
                    if random.random() < 0.5:
                        delai_voiture = random.uniform(1.0, 5.0)
                        print(f"⏰ Voiture aléatoire dans {delai_voiture:.1f}s...")
                        time.sleep(delai_voiture)
                        voiture_detectee()
                        
                elif random.random() < 0.6:  # 30% de chance de voiture seule
                    print("🎲 Action aléatoire: voiture détectée")
                    voiture_detectee()
                else:
                    print("🎲 Action aléatoire: rien ne se passe")
                    time.sleep(2)
                    
            else:
                print("❌ Choix invalide, veuillez réessayer")
                
        except KeyboardInterrupt:
            print("\n👋 Simulation interrompue par l'utilisateur")
            break
        except Exception as e:
            print(f"❌ Erreur lors de la simulation: {e}")

# Version automatique sans interaction utilisateur
def simulation_automatique(duree=60):
    """Simulation automatique pendant une durée définie"""
    print(f"=== DÉMARRAGE DE LA SIMULATION AUTOMATIQUE ({duree}s) ===")
    
    start_time = time.time()
    evenements = []
    
    while time.time() - start_time < duree:
        try:
            # Décision aléatoire
            if random.random() < 0.2:  # 20% de chance d'appui piéton par seconde
                print(f"\n[{int(time.time() - start_time)}s] 👤 Bouton piéton appuyé")
                bouton_pieton_appuye()
                evenements.append("Bouton piéton")
                
                # Voiture potentielle après piéton
                if random.random() < 0.7:  # 70% de chance
                    delai = random.uniform(1.0, 4.0)
                    time.sleep(delai)
                    print(f"[{int(time.time() - start_time)}s] 🚗 Voiture après piéton")
                    voiture_detectee()
                    evenements.append("Voiture après piéton")
                    
            elif random.random() < 0.15:  # 15% de chance de voiture seule
                print(f"\n[{int(time.time() - start_time)}s] 🚗 Voiture détectée")
                voiture_detectee()
                evenements.append("Voiture seule")
                
            time.sleep(1)  # Vérification chaque seconde
            
        except KeyboardInterrupt:
            print("\n👋 Simulation interrompue")
            break
    
    print(f"\n=== FIN DE LA SIMULATION ===")
    print(f"Événements générés: {len(evenements)}")
    for i, event in enumerate(evenements, 1):
        print(f"  {i}. {event}")

# Test
if __name__ == "__main__":
    print("=== CLIENT MODBUS - SIMULATION DE TRAFIC ===")
    print("Choisissez le mode de simulation:")
    print("1. Mode interactif")
    print("2. Mode automatique (60 secondes)")
    
    choix_mode = input("Votre choix (1/2): ").strip()
    
    if choix_mode == "1":
        simulation_trafic()
    elif choix_mode == "2":
        simulation_automatique(60)
    else:
        # Mode par défaut: simple test
        print("Test simple du client Modbus...")
        time.sleep(1)
        bouton_pieton_appuye()
        
        # 70% de chance qu'une voiture arrive après
        if random.random() < 0.7:
            delai = random.uniform(3.0, 7.0)
            print(f"⏰ Une voiture arrivera dans {delai:.1f} secondes...")
            time.sleep(delai)
            voiture_detectee()