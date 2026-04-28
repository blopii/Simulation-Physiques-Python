m =float(input("Entrez le coefficient directeur (pente): "))
p = float(input("Entrez l'ordonnée à l'orgine (altitude initiale):"))
alt_max = float(input("Entrez l'altitude de sécurité: "))
for x in range (16):
   y = m*x+p
   if y > alt_max:
      print(f"[ALERTE] Altitude : {y} m - DANGER!")
   else:
      print(f"Altitude : {y} m - OK.")
