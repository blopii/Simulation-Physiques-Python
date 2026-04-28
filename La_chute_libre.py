h_0= float(input("Entrez l'ordonnée à l'origine (altitude initiale) "))
v_0 = float(input("Entrez la vitesse initial de l'objet: "))
g = float(input("Entrez le seuil de gravité de la planète: "))
for t in range (21):
    z = -0.5 * g * (t**2) + v_0 * t + h_0
    if z >= 0:
        print(f"[t = {t}s] Atitude = {z} m")
    else:
        print(f"L'objet à touché le sol à {t} seconde!") 
        break   



 


