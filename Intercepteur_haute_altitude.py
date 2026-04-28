v_0 = float(input("Indiquez nous la vitesse initiale de l'objet: "))
g = float(input("Indiquez nous le seuil de gravité de la planète: "))
h_target = float(input("Entrez l'altitude du bombardier à intercepter: "))

alt_max = 0
t_apogee = 0
for t in range (41):
    z = -0.5 * g * (t**2) + v_0 * t 
    v = -g * t +v_0
    if z > alt_max:
        alt_max = z 
        t_apogee = t
       
    if v >= 0:
        print(f"[t ={t}s] Altitude: {z}m | Status: ASCENSION")
    else:
        print(f"[t ={t}s] Altitude {z}m | Status: FALLOUT ")    
    
    if z <0:
          print("GROUND CRASH")
          break
        

print(f"Altitude maximale atteinte: {alt_max}m à {t_apogee} secondes.")
if alt_max >= h_target:
 print("TARGET INTERCEPTED! WELL DONE PILOT!")
else:
 print("FAILURE: INSUFFICIENT POWER. THE TARGET IS TOO HIGH.")    
        









