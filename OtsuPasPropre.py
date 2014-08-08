#!/user/amale/home/python2.7

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 17:25:20 2014

@author: amale
"""

import scipy.misc as smisc

import mahotas


path = '/MC70/'
name = 'IMG_05'
ext = '.JPG'
name2 = 'Otsu/IMG_Otsu_05'

for i in range(28,67) :
    
    ##### Reading Image #####
    img = mahotas.imread(path+name+str(i)+ext)
    
#    print img.shape
#    print img.dtype
#    print img.max()
#    print img.min()
    
    ##### Segmentation #####
    T = mahotas.thresholding.otsu(img)

    ##### Saving Image Segmented #####    
    A = img > T
    smisc.imsave(path+name2+str(i)+ext,A)
    
#pl.show()