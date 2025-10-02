# Projet2

# Gestion d'un Feu Tricolore Intelligent

## Problématique

La gestion efficace des feux tricolores est essentielle pour améliorer la fluidité du trafic et réduire les embouteillages. Un feu tricolore intelligent adapte ses cycles en fonction du trafic réel, des piétons et des événements imprévus.

## Objectifs

- Développer un système de feu tricolore capable de détecter le trafic et d'ajuster ses phases automatiquement.
- Intégrer des capteurs pour la détection des véhicules et des piétons.
- Optimiser la sécurité et la rapidité des déplacements.

## Fonctionnalités

- Détection en temps réel du trafic.
- Adaptation dynamique des cycles de feu.
- Priorisation des véhicules d'urgence.
- Interface de monitoring et de configuration.

## Capteurs et Actionneurs Utilisables

Le système peut intégrer différents capteurs et actionneurs, tels que :

- **Capteurs de présence de véhicules** (boucles inductives, capteurs infrarouges, radars)
- **Capteurs de piétons** (boutons poussoirs, capteurs de mouvement, caméras)
- **Capteurs environnementaux** (pluie, luminosité)
- **Actionneurs pour feux tricolores** (relais, modules de commande LED)
- **Systèmes sonores ou lumineux** pour l’alerte des piétons
- **Modules de communication** (Wi-Fi, GSM, LoRa) pour la supervision à distance

## Installation

1. Cloner le dépôt :
    ```bash
    git clone <url-du-repo>
    ```
2. Suivre les instructions du dossier `docs/installation.md`.

## Utilisation

Lancer le système avec :
```bash
python main.py
```

## Contribuer

Les contributions sont les bienvenues ! Veuillez consulter le fichier `CONTRIBUTING.md`.

## Licence

## User Story

**En tant qu'utilisateur piéton**, je souhaite pouvoir appuyer sur un bouton à un passage piéton afin que le feu tricolore détecte ma présence et adapte rapidement le cycle pour me permettre de traverser en toute sécurité, même lorsque le trafic est dense. Ainsi, je me sens en sécurité et je ne dois pas attendre inutilement longtemps.

Ce projet est sous licence MIT.