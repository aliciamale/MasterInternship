#!/user/amale/home/python2.7

# -*- coding: utf-8 -*-
"""
Created on Mon May 19 11:46:01 2014

@author: amale
"""
import scipy as sp
import scipy.misc as smisc
import mahotas
import numpy as np

path = '/MC70/'
path1 = '/MC70/TestGimp/Stats1/'
path2 = '/MC70/TestGimp/Stats2/'
path3 = '/MC70/TestGimp/Stats3/'
pathA = '/MC70/TestGimp/'

name = 'IMG_05'
nameSeg = 'OtsuProprement/IMG_OtsuP_05'
name1 = 'IMG_S1_05' 
name2 = 'IMG_S2_05' 
name3 = 'IMG_S3_05' 
nameS1Seg = 'IMG_S1_OtsuP_05'
nameS2Seg = 'IMG_S2_OtsuP_05'
nameS3Seg = 'IMG_S3_OtsuP_05'
nameA = 'IMG_A_OtsuP_05'

jpg = '.JPG'
png = '.png'
  
def OtsuProprement(img):
    size = np.shape(img)  
    ##### Si on a une image couleur #####
    if np.shape(size) == (3,):   
        ##### Channels Images #####
        red = img[:,:,0]
        green = img[:,:,1]
        blue = img[:,:,2]
        
        ##### Channels Thresholds #####
        Tred = mahotas.thresholding.otsu(red)
        Tgreen = mahotas.thresholding.otsu(green)
        Tblue = mahotas.thresholding.otsu(blue)    
        
        ##### Segmentation #####   
        Ired = red > Tred
        Igreen = green > Tgreen
        Iblue = blue > Tblue
        
        ##### Gathering #####
        B = img.copy()
        B[:,:,0] = Ired
        B[:,:,1] = Igreen
        B[:,:,2] = Iblue
        # B is in uint8, we convert in bool
        B = sp.asarray(B, dtype = bool)
        
        return B
        
    ##### Si on a une image niveau de gris #####
    if np.shape(size) == (2,):
        T = mahotas.thresholding.otsu(img)
        B = img > T
        B = sp.asarray(B, dtype = bool)
        return B
    
    ##### Sinon        
    else:
        print 'Error: image format, try again'

##################### OTSU IMAGES NORMALES ###########################
    
#for i in xrange(28,67):    
#    ##### Reading Image #####
#    image = mahotas.imread(path+name+str(i)+jpg)
#    
#    ##### Application de la Fonction #####
#    imageSeg = OtsuProprement(image)
#    
#    ##### Saving Image Segmented #####    
#    smisc.imsave(path+nameSeg+str(i)+jpg,imageSeg)
    
    
#################### OTSU IMAGES S1, S2, S3, ET S #################### 
     
for i in [28, 29, 32, 33, 37, 42, 47, 52, 57, 62, 66]:
    ##### Reading Image #####
    S1 = mahotas.imread(path1+name1+str(i)+png)
    S2 = mahotas.imread(path2+name2+str(i)+png)
    S3 = mahotas.imread(path3+name3+str(i)+png)
    
    ##### Application de la Fonction #####
    S1Seg = OtsuProprement(S1)
    S2Seg = OtsuProprement(S2)
    S3Seg = OtsuProprement(S3)
    
    #I = mahotas.imread(path+name+str(i)+jpg)
    A = np.empty((2048, 3072, 3))
    A[:,:,0] = S1Seg
    A[:,:,1] = S2Seg
    A[:,:,2] = S3Seg
    
    ##### Saving Image Segmented #####    
    #smisc.imsave(path1+nameS1Seg+str(i)+png, S1Seg)
    #smisc.imsave(path2+nameS2Seg+str(i)+png, S2Seg)
    #smisc.imsave(path3+nameS3Seg+str(i)+png, S3Seg)
    smisc.imsave(pathA+nameA+str(i)+png, A)    
    

    
    
    
    
    
