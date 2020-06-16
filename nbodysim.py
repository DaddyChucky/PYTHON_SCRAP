# Script qui simule l'attraction gravitationnelle des objets de notre système solaire.

import numpy as np
import gc
import time
import math
from vpython import *


class vect:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class initialValuesOfObjects:
    def __init__(self, position, radius, name, mass, velocity, acceleration):
        self.position = position
        self.radius = radius
        self.name = name
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration

sun = initialValuesOfObjects(vect(0,0,0), 696340, "Soleil", 1.989e+30, vect(0,0,0), vect(0,0,0))
earth = initialValuesOfObjects(vect(0,1.5e11,0), 6371, "Terre", 6e24, vect(30000,0,0), vect(0,0,0))
mercury = initialValuesOfObjects(vect(0,5.7e10,0), 2439.7, "Mercure", 3.285e23, vect(47000,0,0), vect(0,0,0))
venus = initialValuesOfObjects(vect(0,1.1e11,0), 6051.8, "Vénus", 4.8e24, vect(35000,0,0), vect(0,0,0))
mars = initialValuesOfObjects(vect(0,2.2e11,0), 3389.5, "Mars", 2.4e24, vect(24000,0,0), vect(0,0,0))
jupiter = initialValuesOfObjects(vect(0,7.7e11,0), 69911, "Jupiter", 1e28, vect(13000,0,0), vect(0,0,0))
saturn = initialValuesOfObjects(vect(0,1.4e12,0), 58232, "Saturne", 5.7e26, vect(9000,0,0), vect(0,0,0))
uranus = initialValuesOfObjects(vect(0,2.8e12,0), 25362, "Uranus", 8.7e25, vect(6835,0,0), vect(0,0,0))
neptune = initialValuesOfObjects(vect(0,4.5e12,0), 24622, "Neptune", 1e26, vect(5477,0,0), vect(0,0,0))
pluto = initialValuesOfObjects(vect(0,3.7e12,0), 1188.3, "Pluton", 1.3e22, vect(4748,0,0), vect(0,0,0))

objects = [[],[],[],[],[],[],[],[], [], [], []] # Création d'un tableau 2d qui stocke les variables des objets

for obj in gc.get_objects():
    if isinstance(obj, initialValuesOfObjects):
        objects[0].append(obj.name)
        objects[1].append(obj.position.x)
        objects[2].append(obj.position.y)
        objects[3].append(obj.position.z)
        objects[4].append(obj.mass)
        objects[5].append(obj.velocity.x)
        objects[6].append(obj.velocity.y)
        objects[7].append(obj.velocity.z)
        objects[8].append(obj.acceleration.x)
        objects[9].append(obj.acceleration.y)
        objects[10].append(obj.acceleration.z)
        
        print("Objet: %s | Position = (%f, %f, %f) | Masse: %f | Vitesse = (%f, %f, %f)\n\n" % (obj.name, obj.position.x, obj.position.y, obj.position.z, obj.mass, obj.velocity.x, obj.velocity.y, obj.velocity.z))

ticks = 50000

print("Objets créés avec succès; variables à l'origine initialisées.\nCalculons l'accélération, la vitesse et la position respective des objets pour les %i prochains ticks.\n" % ticks)

G = 6.67408e-11

accTot = [ [],[],[],[],[],[],[],[],[],[] ],[ [],[],[],[],[],[],[],[],[],[] ],[ [],[],[],[],[],[],[],[],[],[] ] # Format: [Sens acceleration (0-2)][# Objet (0-9)][Vitesse ticks (1-nTicks)] 
velTot = [ [],[],[],[],[],[],[],[],[],[] ],[ [],[],[],[],[],[],[],[],[],[] ],[ [],[],[],[],[],[],[],[],[],[] ] # Format: [Sens vitesse (0-2)][# Objet (0-9)][Vitesse ticks (1-nTicks)] 
posTot = [ [],[],[],[],[],[],[],[],[],[] ],[ [],[],[],[],[],[],[],[],[],[] ],[ [],[],[],[],[],[],[],[],[],[] ] # Format: [Sens position (0-2)][# Objet (0-9)][Vitesse ticks (1-nTicks)]
        
for k in range(10): # L'objet
    for j in range(10): # Tous les autres objets
        if j != k: # L'objet ne s'attire pas lui-même (division par 0)
            a = ( G * objects[4][j] ) / math.sqrt(( (objects[1][k] - objects[1][j])**2 + (objects[2][k] - objects[2][j])**2 + (objects[3][k] - objects[3][j])**2 )**3)
            objects[8][k] += a * (objects[1][j] - objects[1][k]) # Accélération dans l'axe des x
            objects[9][k] += a * (objects[2][j] - objects[2][k]) # Accélération dans l'axe des y
            objects[10][k] += a * (objects[3][j] - objects[3][k]) # Accélération dans l'axe des z
            
for t in range(ticks): # Nombre de secondes de l'historicité
    
    for i in range(10): # L'objet 
    
        if t == 0:
            vx = objects[5][i]
            vy = objects[6][i]
            vz = objects[7][i]
            
            x = objects[1][i]
            y = objects[2][i]
            z = objects[3][i]
        
        else:       
            vx = velTot[0][i][t-1] + accTot[0][i][t-1] * t
            vy = velTot[1][i][t-1] + accTot[1][i][t-1] * t
            vz = velTot[2][i][t-1] + accTot[2][i][t-1] * t
            
            x = posTot[0][i][t-1] + vx * t
            y = posTot[1][i][t-1] + vy * t
            z = posTot[2][i][t-1] + vz * t
            
        
        velTot[0][i].append(vx)
        velTot[1][i].append(vy)
        velTot[2][i].append(vz)
        
        posTot[0][i].append(x)
        posTot[1][i].append(y)
        posTot[2][i].append(z)
    
    
    
    for k in range(10):
        ax = 0 # L'accélération change à chaque intervalle de temps, car la position est modifiée
        ay = 0
        az = 0
        for j in range(10):
            
            if j != k:
                a = ( G * objects[4][j] ) / math.sqrt(( (posTot[0][k][t] - posTot[0][j][t])**2 + (posTot[1][k][t] - posTot[1][j][t])**2 + (posTot[2][k][t] - posTot[2][j][t])**2 )**3)
                ax += a * (posTot[0][j][t] - posTot[0][k][t])
                ay += a * (posTot[1][j][t] - posTot[1][k][t])
                az += a * (posTot[2][j][t] - posTot[2][k][t])
                
        accTot[0][k].append(ax)
        accTot[1][k].append(ay)
        accTot[2][k].append(az)


print("Toutes les accélérations, les vitesses et les positions ont été initialisées. Commencement du schéma interactif sur localhost.\n")

scene = canvas(title="Simulation de notre système solaire (problèmes à n-corps)", width=1700, height=800, center=vector(0,0,0), background=color.white)

sunSphere = sphere(pos = vector(sun.position.x, sun.position.y, sun.position.z), radius=0.4, texture="data:image/jpeg;base64,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")
earthSphere = sphere(pos = vector(earth.position.x/(1e11), earth.position.y/(1e11), earth.position.z/(1e11)), radius=earth.radius/sun.radius*10, texture="https://upload.wikimedia.org/wikipedia/commons/2/22/Earth_Western_Hemisphere_transparent_background.png")
mercurySphere = sphere(pos = vector(mercury.position.x/(1e11), mercury.position.y/(1e11), mercury.position.z/(1e11)), radius=mercury.radius/sun.radius*10, texture="https://upload.wikimedia.org/wikipedia/commons/d/d9/Mercury_in_color_-_Prockter07-edit1.jpg")
venusSphere = sphere(pos = vector(venus.position.x/(1e11), venus.position.y/(1e11), venus.position.z/(1e11)), radius=venus.radius/sun.radius*10, texture="https://upload.wikimedia.org/wikipedia/commons/b/bc/Venuspioneeruv.jpg")
marsSphere = sphere(pos = vector(mars.position.x/(1e11), mars.position.y/(1e11), mars.position.z/(1e11)), radius=mars.radius/sun.radius*10, texture="https://live.staticflickr.com/8192/8145809230_23a9143199_b.jpg")
jupiterSphere = sphere(pos = vector(jupiter.position.x/(1e11), jupiter.position.y/(1e11), jupiter.position.z/(1e11)), radius=jupiter.radius/sun.radius*10, texture="https://live.staticflickr.com/65535/48494223072_7a4bb6ed14_b.jpg")
saturnSphere = sphere(pos = vector(saturn.position.x/(1e11), saturn.position.y/(1e11), saturn.position.z/(1e11)), radius=saturn.radius/sun.radius*10, texture="https://upload.wikimedia.org/wikipedia/commons/5/53/Saturn_-_HST_2019-06-20_full_size.jpg")
uranusSphere = sphere(pos = vector(uranus.position.x/(1e11), uranus.position.y/(1e11), uranus.position.z/(1e11)), radius=uranus.radius/sun.radius*10, texture="https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg")
neptuneSphere = sphere(pos = vector(neptune.position.x/(1e11), neptune.position.y/(1e11), neptune.position.z/(1e11)), radius=neptune.radius/sun.radius*10, texture="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Neptune.jpg/596px-Neptune.jpg")
plutoSphere = sphere(pos = vector(pluto.position.x/(1e11), pluto.position.y/(1e11), pluto.position.z/(1e11)), radius=pluto.radius/sun.radius*100, texture="https://live.staticflickr.com/310/19662931466_c80860b491_b.jpg")

for t in range(ticks - 1):
    rate(1000)
    
    sunSphere.pos=vector(posTot[0][0][t]/(1e11), posTot[1][0][t]/(1e11), posTot[2][0][t]/(1e11))
    #attach_trail(sunSphere, radius=sunSphere.radius/10, color=color.white)
    
    earthSphere.pos=vector(posTot[0][1][t]/(1e11), posTot[1][1][t]/(1e11), posTot[2][1][t]/(1e11))
    #attach_trail(earthSphere, radius=earthSphere.radius/10, color=color.green)

    mercurySphere.pos=vector(posTot[0][2][t]/(1e11), posTot[1][2][t]/(1e11), posTot[2][2][t]/(1e11))
    #attach_trail(mercurySphere, radius=mercurySphere.radius/10, color=color.orange)
    
    venusSphere.pos=vector(posTot[0][3][t]/(1e11), posTot[1][3][t]/(1e11), posTot[2][3][t]/(1e11))
    #attach_trail(venusSphere, radius=venusSphere.radius/10, color=color.cyan)
    
    marsSphere.pos=vector(posTot[0][4][t]/(1e11), posTot[1][4][t]/(1e11), posTot[2][4][t]/(1e11))
    #attach_trail(marsSphere, radius=marsSphere.radius/10, color=color.red)
    
    jupiterSphere.pos=vector(posTot[0][5][t]/(1e11), posTot[1][5][t]/(1e11), posTot[2][5][t]/(1e11))
    #attach_trail(jupiterSphere, radius=jupiterSphere.radius/10, color=color.white)
    
    saturnSphere.pos=vector(posTot[0][6][t]/(1e11), posTot[1][6][t]/(1e11), posTot[2][6][t]/(1e11))
    #attach_trail(saturnSphere, radius=saturnSphere.radius/10, color=color.yellow)
    
    uranusSphere.pos=vector(posTot[0][7][t]/(1e11), posTot[1][7][t]/(1e11), posTot[2][7][t]/(1e11))
    #attach_trail(uranusSphere, radius=uranusSphere.radius/10, color=color.blue)
    
    neptuneSphere.pos=vector(posTot[0][8][t]/(1e11), posTot[1][8][t]/(1e11), posTot[2][8][t]/(1e11))
    #attach_trail(neptuneSphere, radius=neptuneSphere.radius/10, color=color.magenta)
    
    plutoSphere.pos=vector(posTot[0][9][t]/(1e11), posTot[1][9][t]/(1e11), posTot[2][9][t]/(1e11))
    #attach_trail(plutoSphere, radius=plutoSphere.radius/10, color=color.black)
    
# Optimisation à faire:
# Ne mettre aucun trail, car ça lag beaucoup!
# Lancer le programme en 64 bits, utiliser Spyder et non Thonny
# Multithreading pour optimiser les temps de calculs, voire utiliser une librairie C++ pour les arrays
