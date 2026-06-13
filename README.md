# Simulation-Physiques-Python 
Dépôt de travail personnel dédié à la réactivation des bases mathématiques et à l'initiation à la programmation scientifique (Python). L'objectif de ce projet est de lier l'apprentissage de l'algèbre linéaire et de la cinématique à des applications pratiques inspirées du secteur aérospatial.


1.Progression Technique & Mathématique
 Approche Arithmétique & Algorithmique de BaseScripts : 2D.py, 3D.py, intercepteur.py
 Concepts mathématiques : Incrémentation discrète, gestion des repères cartésiens, conditions aux limites (y <= 0).
 Objectif : Prise en main des boucles temporelles pour simuler le déplacement d'un point matériel (drone) à vecteur vitesse   constant ou semi-constant.

2.Modélisation par Fonctions Affines & Cinématique Newtonienne
  Scripts : trajectoire_linéaire.py, La_chute_libre.py, Intercepteur_haute_altitude.py
  Concepts : Équations horaires du mouvement, fonctions affines (type : y = mt + p), polynômes du second degré (type : z =     -0.5 * g * t^2 + v_0 * t).
  Objectif : Traduire les lois de la chute libre verticale sous forme algorithmique. Le script calcule l'évolution de          l'altitude et de la vitesse, et détermine de manière empirique l'apogée de la trajectoire par balayage dans une boucle.

3.Résolution de Systèmes Linéaires (Algorithme de Cramer)
  Scripts : Orbital_rendezvous_solver.py, atmospheric_reentry_corridors.py, vector_thrust_alignment.py
  Concepts : Systèmes d'équations linéaires à deux inconnues (2x2), calcul du déterminant principal (Delta = ad - bc),         théorème de Cramer, étude géométrique de l'intersection de deux droites (cas sécants, colinéaires superposés ou              colinéaires disjoints).
  Objectif : Utiliser l'algèbre linéaire pour résoudre des problèmes d'intersection de trajectoires (rendez-vous orbital ou    couloir de rentrée) et de répartition de contraintes (alignement de poussée vectorielle). Le code identifie de manière       autonome la nature géométrique du système via l'analyse du déterminant (test : Delta != 0).





 
