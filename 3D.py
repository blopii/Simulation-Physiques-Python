#Simulation 3D: trajectoire complète d'un drone avec montée, déplacement multiaxes et phase d'atterrissage
x = 100 
y = -50
z = 20

vx = 10
vy = 5
vz = 6

dt =1 

for t in range (40):
    if t > 10:
        vz = -10
    elif t >6:
        vz = 9
    if vx > 6:
        mvt_x = "avance vers l'Est"    
    elif vx <0:
        mvt_x = "avance vers l'Ouest"    
    else: 
        mvt_x = "reste stable sur l'axe Est-Ouest"  

    if vy >0:
        mvt_y = " Avance vers le Nord"      
    elif vy <0:
        mvt_y = "avance vers le Sud"    
    else:
        mvt_y = "reste stable sur l'axe Nordu-Sud"    

    if vz >0:
        mvt_z = "monte"    
    elif vz < 0:
        mvt_z = "descend"    
    else: 
        mvt_z = 'altitude stable'
    x = x + vx*dt
    y= y + vy*dt
    z = z + vz*dt

    print(f"[t={t}s] Position = ({x}, {y}, {z}) | X : {mvt_x} | Y : {mvt_y} | Z : {mvt_z}")  

    if z <=0:
        print ("Le drone a atteri, fin de la simulation.")  
        break
    elif x >= 200 or y >= 150:
        print("Le drone est sorti de la zone autorisée, fin de la simualation.")
        break



