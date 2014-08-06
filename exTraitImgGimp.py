# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 10:06:09 2014

@author: amale
"""

import mahotas
import scipy.misc as smisc
import numpy as np
#import copy

pathI = '/user/amale/home/Pictures/MC70/'
pathB = '/user/amale/home/Pictures/MC70/IMG_Bonnet/'
path =  '/user/amale/home/Pictures/MC70/TestGimp/'
path1 = '/user/amale/home/Pictures/MC70/TestGimp/Stats1/'
path2 = '/user/amale/home/Pictures/MC70/TestGimp/Stats2/'
path3 = '/user/amale/home/Pictures/MC70/TestGimp/Stats3/'

name = 'IMG_05'
nameB = 'IMG_Bonnet_05'

nameS1 = 'IMG_TestS1_05'
nameS2 = 'IMG_TestS2_05'
nameS3 = 'IMG_TestS3_05'

nameC1 = 'IMG_TestC1_05'
nameC2 = 'IMG_TestC2_05'
nameC3 = 'IMG_TestC3_05'

ext = '.png'


##### Stats IMG_0528 #####
rm1 = 187.
gm1 = 68. 
bm1 = 84.

sigr1 = 94.
sigg1 = 215.
sigb1 = 185.

##### Stats IMG_0542 #####
rm2 = 209.
gm2 = 101. 
bm2 = 123.

sigr2 = 961.
sigg2 = 1000.
sigb2 = 903.

##### Stats IMG_0532 #####
rm3 = 149.
gm3 = 53. 
bm3 = 67.

sigr3 = 499.
sigg3 = 733.
sigb3 = 673.

##### Segmentation functions #####
#def segm(I,l,c):
#    I[l,c,0] = 255
#    I[l,c,1] = 255
#    I[l,c,2] = 255
#def segmS2(I,l,c):
#    I[l,c,0] = 255
#    I[l,c,1] = 255
#    I[l,c,2] = 51
#def segmS3(I,l,c):
#    I[l,c,0] = 0
#    I[l,c,1] = 255
#    I[l,c,2] = 255
    
##### Systeme de vote pour choisir le meilleur jeu de stats pour chaque image #####
for i in [28, 29, 32, 33, 37, 42, 47, 52, 57, 62, 66]:
     
    ##### Reading Image #####
    #imgB = mahotas.imread(pathB+nameB+str(i)+ext)   # image du bonnet 
    img = mahotas.imread(pathI+name+str(i)+'.JPG')   # image de base
    
    PR = img[:,:,0]
    PG = img[:,:,1]
    PB = img[:,:,2] 
    
    #PRb = imgB[:,:,0]
    #PGb = imgB[:,:,1]
    #PBb = imgB[:,:,2]
         
    S1 = (PR - rm1)**2 / sigr1**2 + (PG - gm1)**2 / sigg1**2 + (PB - bm1)**2 / sigb1**2
    S2 = (PR - rm2)**2 / sigr2**2 + (PG - gm2)**2 / sigg2**2 + (PB - bm2)**2 / sigb2**2    
    S3 = (PR - rm3)**2 / sigr3**2 + (PG - gm3)**2 / sigg3**2 + (PB - bm3)**2 / sigb3**2
   
    S = S1 + S2 + S3
    
    #Sb = (PRb - rm1)**2 / sigr1 + (PGb - gm1)**2 / sigg1 + (PBb - bm1)**2 / sigb1
    
    sizeS = S.shape
    sizeImg = img.shape

    MS1 = np.amax(S1)    
    MS2 = np.amax(S2)    
    MS3 = np.amax(S3)
    
    #Mb = np.amax(Sb)
    
    ##### Segmentation #####    
    IS1 = S1 < MS1/10.
    IS2 = S2 < MS2/10.
    IS3 = S3 < MS3/10.    
                
    print 'Image ', name+str(i)+ext, '\n'  
    print 'Taille de S = ', sizeS
    print 'MS1 = ', MS1, 'MS2 = ', MS2, 'MS3 = ', MS3
    print 'MS = ', np.amax(S)
    print "Taille de l'image = ", sizeImg, '\n'
    #print sizeImg1, '\n'
    #print 'S = ', S, '\n'
    
    ##### Saving Image #####   
    
    #smisc.imsave(path+'Vote/IMG_Voted_05'+str(i)+ext,Ielected)

    smisc.imsave(path1+nameS1+str(i)+ext,IS1)
    smisc.imsave(path2+nameS2+str(i)+ext,IS2)    
    smisc.imsave(path3+nameS3+str(i)+ext,IS3)
    
    smisc.imsave(path1+'IMG_S1_05'+str(i)+ext,S1)
    smisc.imsave(path2+'IMG_S2_05'+str(i)+ext,S2)    
    smisc.imsave(path3+'IMG_S3_05'+str(i)+ext,S3)

#    smisc.imsave(path+'IMG_S_05'+str(i)+ext,S)    
