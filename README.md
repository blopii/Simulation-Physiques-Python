# Simulation-Physiques-Python
Dépôt regroupant mes travaux d'auto-formation en Python : modélisation de trajectoires, dynamique de vol et algorithmes de calcul physique
# Simulations Physiques et Mathématiques (Python)

Ce dépôt présente ma progression en programmation et en modélisation, illustrant mon passage d'une approche arithmétique simple à l'utilisation de l'algèbre pour la simulation de vol.

## Projets (Ordre de progression réelle)

### 1. Simulateur de Drone 3D (3D.py)
- Niveau : Arithmétique
- Notion : Gestion de coordonnées X, Y, Z par incrémentation
- Description : Mon premier script de mouvement. Il gère la trajectoire d'un drone (décollage, navigation et atterrissage) par de simples additions et soustractions de coordonnées.

### 2. Simulation de Trajectoire Simple (trajectoire_linéaire.py)
- Niveau : Algèbre de base
- Notion : La fonction affine y = mt + y0
- Description : Passage à la modélisation mathématique pour lier précisément l'altitude au temps de vol à l'aide d'une pente constante.

### 3. Générateur de Rapport de Vol (Générateur_de_rapport_de_vol.py)
- Niveau : Automatisation technique
- Notion : Structuration de données et export
- Description : Outil permettant de structurer les résultats des simulations et d'exporter un rapport technique lisible pour une analyse post-vol.

### 4. Algorithme d'Interception Standard (intercepteur.py)
- Niveau : Logique algorithmique et détection
- Notion : Conditions d'arrêt et surveillance d'impact (y <= 0)
- Description : Simulation de trajectoire jusqu'à l'impact au sol avec introduction d'une condition de sortie de boucle automatique dès que l'objectif est atteint.

### 5. Analyse de la Chute Libre (La_chute_libre.py)
- Niveau : Physique Newtonienne (Intermédiaire)
- Notion : Signe de la pente et interprétation du mouvement
- Description : Simulation capable d'interpréter le coefficient directeur pour annoncer de manière autonome si l'avion est en phase de montée ou de descente.

### 6. Calculateur d'Interception Haute Altitude (Intercepteur_haute_altitude.py)
- Niveau : Analyse complexe (Expert)
- Notion : Comparaison de trajectoires multiples et calcul d'apogée
- Description : Projet le plus avancé. Il suit deux objets en parallèle pour prédire et calculer un point d'interception précis entre une cible et un intercepteur.
