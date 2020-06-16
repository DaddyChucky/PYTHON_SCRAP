# Interview Google : "Nous avons une fonction quelconque qui calcule tous les nombres de 0 à 1 de façon uniforme. Calculez pi."

# ---- PROCESSUS ----
# Supposons un cercle de rayon 1 centré en (0,0) (x^2 + y^2 = 1) où l'aire = pi * r^2
# Supposons un carré qui inclut ce cercle de côté 1 (aire = r^2)
# Si nous prenons seulement le second quadrant et que nous comptons le nombre de points qui figurent dans le cercle qui respectent les
# conditions x > 0 et y > 0 ; et que nous comptons le nombre de points qui figurent dans le carré du second quadrant (respectant aussi
# les conditions x > 0 et y > 0 ; alors le rapport (points cercle 2e quadrant) / (points cercle 2e quadrant + carré 2e quadrant) est
# équivalent au rapport (points cercle des 4 quadrants) / (points carré des 4 quadrants)
# Pour parvenir à résoudre le problème, nous allons créer une fonction qui ajoute des points au hasard dans le premier quadrant (1),
# vérifier que ces points se situent à l'intérieur du cercle (norme <= 1) ou à l'extérieur (norme > 1) (2), établir le rapport entre le
# nombre de points du cercle et le nombre de points total du carré (premier quadrant) (3), avant d'enfin isoler pi grâce à la formule
# de l'aire du cercle

import random
import numpy as np
import matplotlib.pyplot as plt
import math

def estimatePi(n): # n étant le nombre de points total
    
    r = 1 # rayon cercle
    
    a = []
    b = []
    
    nbCercle = 0 
    nbTot = 0
        
    for i in range(n):
        
        rA = random.uniform(0, 1)
        rB = random.uniform(0, 1)
        randomA = [rA]
        randomB = [rB]
        
        # ---- ÉVITER LES POINTS EN DOUBLE ----
        if randomA in a and randomB in b:
            if a[randomA] == a[randomB]:
                print("Collision détectée, vous êtes chanceux ! Point non compté dans l'évaluation.")
        else:
            a.append(randomA)
            b.append(randomB)
        
        # ---- CALCULONS LE NOMBRE DE POINTS DANS LE CERCLE ET CELUI TOTAL ----     
        norme = abs(math.sqrt(rA**2 + rB**2)) # x^2 + y^2 = norme^2
  
        if norme <= 1: # dans le cercle
            nbCercle = nbCercle + 1
        else:
            nbTot = nbTot + 1
        
    nbTot = nbTot + nbCercle 
    print(nbCercle/nbTot*4)       
           
    # ---- BORDURES ----
    xLim = np.array([0,1])
    yLim = np.array([0,1])
    
    # Carré
    plt.plot(xLim, (0,0), color="blue", linestyle="dashed")
    plt.plot(xLim, (1,1), color="blue", linestyle="dashed")
    plt.plot((0,0), yLim, color="blue", linestyle="dashed")
    plt.plot((1,1), yLim, color="blue", linestyle="dashed")
    
    # Sphère
    x = []
    y = []
    
    for j in range(100000):
        insertX = r / 100000 * j
        x.append(insertX)

        y.append(abs(math.sqrt((1-insertX**2)))) # x^2 + y^2 = 1, on a isolé y et retenu que la valeur positive
    
    plt.plot(x,y, color="green", linestyle="solid")
    
    plt.plot(a,b,'ro')
    plt.axis([-0.1,1.1,-0.1,1.1])
    plt.show()
            
        
    
estimatePi(10000) # Changer pour la valeur souhaitée, plus il y a de points, plus l'estimation est valide