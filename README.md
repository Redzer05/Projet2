# Projet2

# Gestion d'un Feu Tricolore Intelligent

## Problématique

La gestion efficace des feux tricolores est essentielle pour améliorer la fluidité du trafic et réduire les embouteillages. Un feu tricolore intelligent adapte ses cycles en fonction du trafic réel, des piétons et des événements imprévus.

## Objectifs

- Développer un système client-serveur pour la gestion intelligente des feux tricolores.
- Permettre la détection du trafic et l'ajustement automatique des phases via le serveur.
- Intégrer des capteurs pour la détection des véhicules et des piétons côté client.
- Optimiser la sécurité et la rapidité des déplacements.

## Architecture

Le projet est composé de deux parties principales :
- **Serveur** : Centralise la logique de gestion des cycles, reçoit les données des capteurs, prend les décisions et envoie les commandes aux clients.
- **Client** : Représente un feu tricolore, collecte les données des capteurs locaux (véhicules, piétons, environnement), affiche l'état du feu et exécute les ordres reçus du serveur.

La communication entre le client et le serveur se fait via des sockets (TCP/IP).

## Fonctionnalités

- Détection en temps réel du trafic et des piétons (côté client).
- Transmission des données de capteurs du client vers le serveur.
- Adaptation dynamique des cycles de feu par le serveur.
- Priorisation des véhicules d'urgence.
- Interface de monitoring et de configuration (côté serveur).
- Supervision à distance via modules de communication.

## Capteurs et Actionneurs Utilisables

Le système peut intégrer différents capteurs et actionneurs, tels que :

- **Capteurs de présence de véhicules** (boucles inductives, capteurs infrarouges, radars)
- **Capteurs de piétons** (boutons poussoirs, capteurs de mouvement, caméras)
- **Capteurs environnementaux** (pluie, luminosité)
- **Actionneurs pour feux tricolores** (relais, modules de commande LED)
- **Systèmes sonores ou lumineux** pour l’alerte des piétons
- **Modules de communication** (Wi-Fi, GSM, LoRa) pour la supervision à distance

## Installation

1. Cloner le dépôt :
    ```bash
    git clone <url-du-repo>
    ```
2. Installer les dépendances côté serveur et client :
    ```bash
    cd server
    pip install -r requirements.txt

    cd ../client
    pip install -r requirements.txt
    ```
3. Suivre les instructions du dossier `docs/installation.md` pour la configuration des capteurs et des adresses réseau.

## Utilisation

- **Lancer le serveur** :
    ```bash
    cd server
    python server.py
    ```
- **Lancer un client (feu tricolore)** :
    ```bash
    cd client
    python client.py
    ```

## Contribuer

Les contributions sont les bienvenues ! Veuillez consulter le fichier `CONTRIBUTING.md`.

## Licence

Ce projet est sous licence MIT.

## User Story

**En tant qu'utilisateur piéton**, je souhaite pouvoir appuyer sur un bouton à un passage piéton afin que le feu tricolore détecte ma présence et adapte rapidement le cycle pour me permettre de traverser en toute sécurité, même lorsque le trafic est dense. Ainsi, je me sens en sécurité et je ne dois pas attendre inutilement longtemps.