import os
import random as rd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# CONSTANTES
fillValue = -888.80
xValue = -111
noneValue = -222
iceValue = -1.80

# CREATION MATTEMP
matTemp = []

def init_matTemp(matrice = matTemp):

    os.chdir("../TIPE 2019/dataset_weeks/SST_training_dataset")
    listFile = os.listdir()
    listFile.sort()
    if matrice == []:
        for fichier in listFile:
            matriceSemaine = []
            f = open(fichier,'r')
            for i in range(6): f.readline()
            for i in range(180):
                matriceSemaine += [[float(i) for i in f.readline().split()]]
                matrice.append(matriceSemaine)
            print(fichier," OK")
        print("matTemp OK")

# CARTE
def show_map(mat):
    plt.imshow(mat, cmap='jet', vmin = -10)
    plt.show()

fig = plt.figure(figsize = (12,7))
init_matTemp()
show_map(matTemp[0])

# im = plt.imshow(matTemp[0], animated=True, cmap='jet', vmin = -10)
#
# n = 0
# def updatefig(*args):
#     global n
#     n = (n+1) % 100
#     im.set_array(matTemp[n])
#     return im,
#
# ani = animation.FuncAnimation(fig, updatefig, interval=1000)
# plt.show()

# def animate_map():
#     fig = plt.figure()
#     im = plt.imshow(matTemp[0], animated=True, cmap='jet', vmin = -10)
#
#     def updatefig(*args):
#         global n
#         n = (n+1)
#         im.set_array(matTemp[n])
#         return im,
#
#
#     ani = animation.FuncAnimation(fig, updatefig, interval = 200)
#     plt.show()
# animate_map()
