# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 16:53:56 2014

@author: amale
"""

import numpy as np
import mahotas


path1 = '/user/amale/home/Pictures/MC70/TestGimp/Stats1/'
path2 = '/user/amale/home/Pictures/MC70/TestGimp/Stats2/'
path3 = '/user/amale/home/Pictures/MC70/TestGimp/Stats3/'

name = 'IMG_05'
name1 = 'IMG_S1_05'
name2 = 'IMG_S2_05'
name3 = 'IMG_S3_05'

ext = '.png'

for i in [28, 32, 37, 42, 47, 52, 57, 62, 66]:
     
    ##### Reading Image #####
    img1 = mahotas.imread(path1+name1+str(i)+ext)    
    img2 = mahotas.imread(path2+name2+str(i)+ext)
    img3 = mahotas.imread(path3+name3+str(i)+ext)
    
    size = img1.shape    
            
    moy1 = np.mean(img1)
    var1 = np.var(img1)
    max1 = np.amax(img1)
    min1 = np.amin(img1)
    
    moy2 = np.mean(img2)
    var2 = np.var(img2)
    max2 = np.amax(img2)
    min2 = np.amin(img2)
    
    moy3 = np.mean(img3)
    var3 = np.var(img3)
    max3 = np.amax(img3)
    min3 = np.amin(img3)
    
    print 'Image ', name+str(i)+ext, '\n'  
    print 'S1 : moyenne = ', moy1, '/ variance = ', var1, '/ maximum = ', max1, '/ minimum = ', min1
    print 'S2 : moyenne = ', moy2, '/ variance = ', var2, '/ maximum = ', max2, '/ minimum = ', min1
    print 'S3 : moyenne = ', moy3, '/ variance = ', var3, '/ maximum = ', max3, '/ minimum = ', min1, '\n'
    
    