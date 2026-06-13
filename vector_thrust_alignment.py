a = float(input("[INPUT] Moteur A - Efficacité Alpha: "))
b = float(input("[INPUT] Moteur A - Efficacité Beta: "))
e = float(input("[INPUT] Moteur A - Consigne Tangage: "))
c = float(input("[INPUT] Moteur B - Effacité Alpha: "))
d = float(input("[INPUT] Moteur B - Efficacité Beta: "))
f = float(input("[INPUT] Moteur B - Consigne Tangage: "))

Delta = a*d - b*c
if Delta != 0:
    Dx = e*d - b*f
    Dy = a*f - c*e
    x = Dx/Delta
    y = Dy/Delta
    print("[✓] STATUT : Solution de poussé unique trouvée. ")
    print(f"[•] Temps d'allumage Moteur A (x): {x}s ")
    print(f"[•] Temps d'allumage Moteur B (y): {y}s ")
else:
     if (f*a == e*c) and (f*b == e*d):
        print("[SÉCURITÉ] ATTENTION : Profils de poussée redondants. ")
        print("[•] Statut : Les moteurs agissent sur les memes vecteurs. ")
        print("[•] Action : Infinité de combinaisons possibles pour stabiliser le module. ")
     else: 
        print("[CRASH AVORTÉ] ERREUR CRITIQUE D'ALIGNEMENT")  
        print("[•] Statut : Poussées colinéaires mais consigne contradictoires.")  
        print("[•] Action : Impossible de stabiliser le module. Correction physique irréalisable.")


    
        
