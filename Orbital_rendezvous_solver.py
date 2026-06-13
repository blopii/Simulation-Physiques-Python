a = float(input("Entrez le coefficient a (Station - axe X): "))
b = float(input("Entrez le coefficient b (Station - axe Y): "))
e = float(input("Entrez la constante e (Station - vecteur d'état): "))
c = float(input("Entrez le coefficient c (Cargo - axe X): "))
d = float(input("Entrez le coefficient d (Cargo - axe Y): "))
f = float(input("Entrez la constante f (Cargo - vecteur d'état): "))

Delta = a*d - b*c
Dx = e*d - b*f
Dy = a*f - c*e

if Delta != 0:
    x = Dx/Delta
    y = Dy/Delta
    print("=" *60)
    print("   SIMULATEUR DE RENDEZ-VOUS ORBITAL - MISSION CARGO-ISS   ")
    print("="*60)
    print("[+] Paramètres d'approche enregistrés.")
    print(f"[•] Delta = {Delta}")
    print(f"\n[✓] STATUT: Trajectoires sécantes. Fenêtre d'amarrage valide.")
    print(f"\n[RÉSULTAT DE MISSION]")
    print(f"-> Temps de contact requis (x) : {x} s")
    print(f"-> Position relative cible (y) : {y} m")
    print("="*60)
   

else:
    print("="*60)
    print("   SIMULATEUR DE RENDEZ-VOUS ORBITAL - MISSION CARGO-ISS   ")
    print("="*60)
    print("[+] Paramètres d'approche enregistrés.")
    print("[•] Calcul du Déterminant Principal...")
    print("[•] Delta = 0.0")
    print("\n[ALERTE] FENÊTRE D'AMARRAGE IMPOSSIBLE")
    print(" -> Statut : Les trajectoires sont parallèles ou confondues.")
    print(" -> Missions : Avortée. Pas de point d'intersection possible.")
    print("="*60)
    