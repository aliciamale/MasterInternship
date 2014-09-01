import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import mahotas
import scipy.misc as smisc
import numpy as np

pathI = 'MC70/'
pathB = 'MC70/IMG_Bonnet/'
path =  'MC70/TestGimp/'
path1 = 'MC70/TestGimp/Stats1/'
path2 = 'MC70/TestGimp/Stats2/'
path3 = 'MC70/TestGimp/Stats3/'

name = 'IMG_05'
nameB = 'IMG_Bonnet_05'

nameS1 = 'IMG_TestS1_05'
nameS2 = 'IMG_TestS2_05'
nameS3 = 'IMG_TestS3_05'

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

for i in [28, 29, 32, 33, 37, 42, 47, 52, 57, 62, 66]:
     
    ##### Lecture Image #####
    imgB = mahotas.imread(pathB+nameB+str(i)+ext)   # image du bonnet
    img = mahotas.imread(pathI+name+str(i)+'.JPG')   # image de base
    
    # Canaux RGB image normale #
    PR = img[:,:,0]
    PG = img[:,:,1]
    PB = img[:,:,2] 
    
    # Canaux RGB image bonnet #
    PRb = imgB[:,:,0]
    PGb = imgB[:,:,1]
    PBb = imgB[:,:,2]
    
    # Calculs moyennes et variances sur les canaux image bonnet #
    rmb = np.mean(PRb)
    gmb = np.mean(PGb)
    bmb = np.mean(PBb)
    
    sigrb = np.var(PRb)
    siggb = np.var(PGb)
    sigbb = np.var(PBb)
    
    ##### Calculs criteres #####
    S1 = (PR - rm1)**2 / sigr1 + (PG - gm1)**2 / sigg1 + (PB - bm1)**2 / sigb1
    S2 = (PR - rm2)**2 / sigr2 + (PG - gm2)**2 / sigg2 + (PB - bm2)**2 / sigb2
    S3 = (PR - rm3)**2 / sigr3 + (PG - gm3)**2 / sigg3 + (PB - bm3)**2 / sigb3
   
    S = S1 + S2 + S3
    
    Sb = (PRb - rmb)**2 / sigrb + (PGb - gmb)**2 / siggb + (PBb - bmb)**2 / sigbb
    Mb = np.amax(Sb)
    
    ##### Segmentation #####    
    IS1 = S1 < Mb
    IS2 = S2 < Mb
    IS3 = S3 < Mb
    
    ISU1 = 255 * IS1.astype(np.uint8)
    ISU2 = 255 * IS2.astype(np.uint8)
    ISU3 = 255 * IS3.astype(np.uint8)
    
    ##### Enregistrement Image #####
    smisc.imsave(path1+nameS1+str(i)+ext,ISU1)
    smisc.imsave(path2+nameS2+str(i)+ext,ISU2)
    smisc.imsave(path3+nameS3+str(i)+ext,ISU3)
    
    smisc.imsave(path1+'IMG_S1_05'+str(i)+ext,S1)
    smisc.imsave(path2+'IMG_S2_05'+str(i)+ext,S2)
    smisc.imsave(path3+'IMG_S3_05'+str(i)+ext,S3)

    smisc.imsave(path+'IMG_S_05'+str(i)+ext,S)
