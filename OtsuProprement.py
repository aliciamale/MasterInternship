import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import scipy as sp
import scipy.misc as smisc
import mahotas
import numpy as np

path = 'MC70/'
path1 = 'MC70/TestGimp/Stats1/'
path2 = 'MC70/TestGimp/Stats2/'
path3 = 'MC70/TestGimp/Stats3/'
pathA = 'MC70/TestGimp/'

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
        
        IUred = 255 * Ired.astype(np.uint8)
        IUgreen = 255 * Igreen.astype(np.uint8)
        IUblue = 255 * Iblue.astype(np.uint8)
        
        ##### Gathering #####
        B = img.copy()
        B[:,:,0] = IUred
        B[:,:,1] = IUgreen
        B[:,:,2] = IUblue
        # B is in uint8, we convert in bool
        #B = sp.asarray(B, dtype = bool)
        
        return B
        
    ##### Si on a une image niveau de gris #####
    if np.shape(size) == (2,):
        T = mahotas.thresholding.otsu(img)
        B = img > T
        BU = 255 * B.astype(np.uint8)
        return BU
    
    ##### Sinon        
    else:
        print 'Error: image format, try again'

##################### OTSU IMAGES NORMALES ###########################
    
for i in xrange(28,67):    
    ##### Reading Image #####
    image = mahotas.imread(path+name+str(i)+jpg)
    
    ##### Application de la Fonction #####
    imageSeg = OtsuProprement(image)
    
    ##### Saving Image Segmented #####    
    smisc.imsave(path+nameSeg+str(i)+jpg,imageSeg)


    

    
    
    
    
    
