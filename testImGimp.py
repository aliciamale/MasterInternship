# -*- coding: utf-8 -*-
"""
Created on Wed May 21 12:07:22 2014

@author: amale
"""

#import scipy.misc as smisc
import numpy as np
import mahotas


path1 = '/user/amale/home/Pictures/MC70/IMG_Bonnet/'
path2 = '/user/amale/home/Pictures/MC70/IMG_ElectrodesVertes/'
path3 = '/user/amale/home/Pictures/MC70/IMG_ElectrodesBlanches/'
path4 = '/user/amale/home/Pictures/MC70/IMG_ElectrodesNoires/'

name = 'IMG_05'
name1 = 'IMG_Bonnet_05'
name2 = 'IMG_ElectrodesVertes_05'
name3 = 'IMG_ElectrodesBlanches_05'
name4 = 'IMG_ElectrodesNoires_05'

ext = '.png'

#name2 = '/IMG_Otsu_05'

#### Calculs sur le bonnet ####
for i in [28, 32, 37, 42, 47, 52, 57, 62, 66]:
     
    ##### Reading Image #####
    img1 = mahotas.imread(path1+name1+str(i)+ext)    
    img2 = mahotas.imread(path2+name2+str(i)+ext)
    img3 = mahotas.imread(path3+name3+str(i)+ext)
    img4 = mahotas.imread(path4+name4+str(i)+ext)
    
    size = img1.shape 
    nblig = size[0]    
    nbcol = size[1]
    
#    PR1 = []    
#    PG1 = []
#    PB1 = []
#    
#    PR2 = []
#    PG2 = []
#    PB2 = []
#
#    PR3 = []
#    PG3 = []
#    PB3 = []
#    
#    PR4 = []
#    PG4 = []
#    PB4 = []
    
    ### Il faut que la moyenne corresponde a une couleur moyenne
    ### On dirait que l'image n'a pas le fond transparent
    ### donc il faut recreer les images avec le fond transparent (png)
    ### Puis faire une boucle sur la 4e composante de l'image 
    ### (0 -> transparent, 255 -> opaque, entre les deux -> visible)
    ### Prendre en compte uniquement px visibles (px != 0) pour faire les stats              

    PR1 = img1[:,:,0]
    PG1 = img1[:,:,1]
    PB1 = img1[:,:,2]
    
    PR2 = img2[:,:,0]
    PG2 = img2[:,:,1]
    PB2 = img2[:,:,2]

    PR3 = img3[:,:,0]
    PG3 = img3[:,:,1]
    PB3 = img3[:,:,2]

    PR4 = img4[:,:,0]
    PG4 = img4[:,:,1]
    PB4 = img4[:,:,2]    
    
    elt_del1 = [(nbcol*l + c+1) - 1 for l in xrange(nblig) for c in xrange(nbcol) if  img1[l,c,3] == 0]  
    PR1 = np.delete(PR1, elt_del1)
    PG1 = np.delete(PG1, elt_del1)
    PB1 = np.delete(PB1, elt_del1)
    
    elt_del2 = [(nbcol*l + c+1) - 1 for l in xrange(nblig) for c in xrange(nbcol) if  img2[l,c,3] == 0]  
    PR2 = np.delete(PR2, elt_del2)
    PG2 = np.delete(PG2, elt_del2)
    PB2 = np.delete(PB2, elt_del2)
    
    elt_del3 = [(nbcol*l + c+1) - 1 for l in xrange(nblig) for c in xrange(nbcol) if  img3[l,c,3] == 0]  
    PR3 = np.delete(PR3, elt_del3)
    PG3 = np.delete(PG3, elt_del3)
    PB3 = np.delete(PB3, elt_del3)
    
    elt_del4 = [(nbcol*l + c+1) - 1 for l in xrange(nblig) for c in xrange(nbcol) if  img4[l,c,3] == 0]  
    PR4 = np.delete(PR4, elt_del4)
    PG4 = np.delete(PG4, elt_del4)
    PB4 = np.delete(PB4, elt_del4)
    
#    for j in xrange(size[0]):
#        for k in xrange(size[1]):
#            if img1[j,k,3] != 0:
#                pxR1 = img1[j,k,0]
#                pxG1 = img1[j,k,1]
#                pxB1 = img1[j,k,2]                
#                PR1 = np.append(PR1, pxR1)
#                PG1 = np.append(PG1, pxG1)
#                PB1 = np.append(PB1, pxB1)             
#            if img2[j,k,3] != 0:
#                pxR2 = img2[j,k,0]
#                pxG2 = img2[j,k,1]
#                pxB2 = img2[j,k,2]                
#                PR2 = np.append(PR2, pxR2)
#                PG2 = np.append(PG2, pxG2)
#                PB2 = np.append(PB2, pxB2)
#            if img3[j,k,3] != 0:
#                pxR3 = img3[j,k,0]
#                pxG3 = img3[j,k,1]
#                pxB3 = img3[j,k,2]                
#                PR3 = np.append(PR3, pxR3)
#                PG3 = np.append(PG3, pxG3)
#                PB3 = np.append(PB3, pxB3)  
#            if img4[j,k,3] != 0:
#                pxR4 = img4[j,k,0]
#                pxG4 = img4[j,k,1]
#                pxB4 = img4[j,k,2]                
#                PR4 = np.append(PR4, pxR4)
#                PG4 = np.append(PG4, pxG4)
#                PB4 = np.append(PB4, pxB4)       
#    
    ##### Bonnet #####
    
    moyR1 = np.mean(PR1)
    moyG1 = np.mean(PG1)
    moyB1 = np.mean(PB1)
    
    colorMoy1 = [moyR1, moyG1, moyB1]
    
    varR1 = np.var(PR1)
    varG1 = np.var(PG1)
    varB1 = np.var(PB1)
    
    RGBVar1 = [varR1, varG1, varB1]
    
    ##### Electrodes Vertes ######    
    
    moyR2 = np.mean(PR2)
    moyG2 = np.mean(PG2)
    moyB2 = np.mean(PB2)                   
    
    colorMoy2 = [moyR2, moyG2, moyB2]

    varR2 = np.var(PR2)
    varG2 = np.var(PG2)
    varB2 = np.var(PB2)
    
    RGBVar2 = [varR2, varG2, varB2]
    
    ##### Electrodes Blanches #####
           
    moyR3 = np.mean(PR3)
    moyG3 = np.mean(PG3)
    moyB3 = np.mean(PB3)    
             
    colorMoy3 = [moyR3, moyG3, moyB3]             

    varR3 = np.var(PR3)
    varG3 = np.var(PG3)
    varB3 = np.var(PB3)
           
    RGBVar3 = [varR3, varG3, varB3]           
           
    ##### Electrodes Noires #####             
             
    moyR4 = np.mean(PR4)
    moyG4 = np.mean(PG4)
    moyB4 = np.mean(PB4)    
                   
    colorMoy4 = [moyR4, moyG4, moyB4]
                  
    varR4 = np.var(PR4)
    varG4 = np.var(PG4)
    varB4 = np.var(PB4)
    
    RGBVar4 = [varR4, varG4, varB4]    
    
    ##### Affichage #####
            
    print 'Image ', name+str(i)+ext, '\n'    
    
    print 'Couleur Moyenne Bonnet = ', colorMoy1
    print 'Couleur Moyenne Electrodes Vertes = ', colorMoy2
    print 'Couleur Moyenne Electrodes Blanches = ', colorMoy3
    print 'Couleur Moyenne Electrodes Noires = ', colorMoy4
    
    print 'Variances RGB Bonnet = ', RGBVar1
    print 'Variances RGB Electrodes Vertes = ', RGBVar2
    print 'Variances RGB Electrodes Blanches = ', RGBVar3
    print 'variances RGB Electrodes Noires = ', RGBVar4, '\n'
    
    ##### Threshold Calcul #####
    #T = mahotas.thresholding.otsu(img)
                