import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import scipy.misc as smisc
import mahotas
import numpy as np

path = 'MC70/'
name = 'IMG_05'
ext = '.JPG'
name2 = 'Otsu/IMG_Otsu_05'

for i in range(28,67) :
    
    ##### Reading Image #####
    img = mahotas.imread(path+name+str(i)+ext)
    
    ##### Segmentation #####
    T = mahotas.thresholding.otsu(img)
    A = img > T
    AU = 255 * A.astype(np.uint8)
    
    ##### Saving Image Segmented #####
    smisc.imsave(path+name2+str(i)+ext,AU)