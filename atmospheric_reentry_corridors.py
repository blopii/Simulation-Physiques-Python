a = float(input("[INPUT] Capsule A - Facteur aérodinamique Alpha: "))
b = float(input("[INPUT] Capsule A - Facteur aérodynamique Beta: "))
e = float(input("[INPUT] Capsule A - Constante d'altitude critique: "))

c = float(input("[INPUT] Capsule B - Facteur aérodynamique Alpha:"))
d = float(input("[INPUT] Capsule B - Facteur aérodynamique Beta:"))
f = float(input("[INPUT] Capsule B - Constante d'altitude critique:"))

A = -a
B = -b
C = c 
D = -d
E = e
F = -f

Delta = (A*D - B*C)
if Delta != 0:
    Dx = (E*D - B*F)
    Dy = (A*F - E*C)
    x = Dx/Delta
    y = Dy/Delta
    print("[✓] Statut : Trajectoires sécantes détectées.")
    print(f"[•] Coordonnées temporelle de contact (x): {x}s")
    print(f"[•] Coordonées d'altitude relative (y): {y}m")
else:
   
    if F*A== E*C:
        print("[ALERTE CRITIQUE] DANGER DE COLLISION FRONTALE")
        print("[•] Les couloirs de rentrée sont parfaitement superposés.")
        print("[•] Missison : Interception phyisique inévitable sur la trajectoire actuelle.]")
    else:
        print("[CONFIRMATION] SÉCURITÉ DES TRAJECTOIRES VALIDÉE")
        print("[•] Statut : Les couloirs de rentrée sont strictement parrallèles et disjoints. ")
        print("[•] Aucune intersection possible. Les capsules sont sur des rails séparés.")
   
        


   