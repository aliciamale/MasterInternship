import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import numpy as np
from numpy import linalg as la
import scipy.misc as smisc
import scipy as sp
import mahotas
#import copy

path = 'MC70/'
pathB = 'MC70/IMG_Bonnet/'
name = 'IMG_05'
nameB = 'IMG_Bonnet_05'
ext = '.JPG'
    
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
        
    ##### Si on a une image niveaux de gris #####
    if np.shape(size) == (2,):
        T = mahotas.thresholding.otsu(img)
        B = img > T
        B = sp.asarray(B, dtype = bool)
        return B
    
    ##### Sinon        
    else:
        print 'Error: image format, try again'
        
seuil = 100000  # max = 163000, min = 0

pathEIG_VPgde = 'MC70/IMG_Bonnet/VPgde/pxTranspSup'+str(seuil)+'/EIG/'
pathEIG_VPmed = 'MC70/IMG_Bonnet/VPmed/pxTranspSup'+str(seuil)+'/EIG/'
pathEIG_VPpet = 'MC70/IMG_Bonnet/VPpet/pxTranspSup'+str(seuil)+'/EIG/'

pathSVD_VPgde = 'MC70/IMG_Bonnet/VPgde/pxTranspSup'+str(seuil)+'/SVD/'
pathSVD_VPmed = 'MC70/IMG_Bonnet/VPmed/pxTranspSup'+str(seuil)+'/SVD/'
pathSVD_VPpet = 'MC70/IMG_Bonnet/VPpet/pxTranspSup'+str(seuil)+'/SVD/'

pathSVD_UPgde = 'MC70/IMG_Bonnet/UPgde/pxTranspSup'+str(seuil)+'/'
pathSVD_UPmed = 'MC70/IMG_Bonnet/UPmed/pxTranspSup'+str(seuil)+'/'
pathSVD_UPpet = 'MC70/IMG_Bonnet/UPpet/pxTranspSup'+str(seuil)+'/'

pathEIG_VPgde_BS = 'MC70/IMG_Bonnet/VPgde/pxTranspSup'+str(seuil)+'/EIG/BeforeSegm/'
pathEIG_VPmed_BS = 'MC70/IMG_Bonnet/VPmed/pxTranspSup'+str(seuil)+'/EIG/BeforeSegm/'
pathEIG_VPpet_BS = 'MC70/IMG_Bonnet/VPpet/pxTranspSup'+str(seuil)+'/EIG/BeforeSegm/'

pathSVD_VPgde_BS = 'MC70/IMG_Bonnet/VPgde/pxTranspSup'+str(seuil)+'/SVD/BeforeSegm/'
pathSVD_VPmed_BS = 'MC70/IMG_Bonnet/VPmed/pxTranspSup'+str(seuil)+'/SVD/BeforeSegm/'
pathSVD_VPpet_BS = 'MC70/IMG_Bonnet/VPpet/pxTranspSup'+str(seuil)+'/SVD/BeforeSegm/'

pathSVD_UPgde_BS = 'MC70/IMG_Bonnet/UPgde/pxTranspSup'+str(seuil)+'/BeforeSegm/'
pathSVD_UPmed_BS = 'MC70/IMG_Bonnet/UPmed/pxTranspSup'+str(seuil)+'/BeforeSegm/'
pathSVD_UPpet_BS = 'MC70/IMG_Bonnet/UPpet/pxTranspSup'+str(seuil)+'/BeforeSegm/'

###### Meme chose sur les images de bonnet extrait en enlevant les px transparents et ceux trop pres du blanc #####
for i in [28, 29, 32, 33, 37, 42, 47, 52, 57, 62, 66]:
    
    nameEIG_VPgde = 'IMG_VPgde_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameEIG_VPmed = 'IMG_VPmed_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameEIG_VPpet = 'IMG_VPpet_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'

    nameSVD_VPgde = 'IMG_VPgde(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_VPmed = 'IMG_VPmed(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_VPpet = 'IMG_VPpet(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'

    nameSVD_UPgde = 'IMG_UPgde(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_UPmed = 'IMG_UPmed(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_UPpet = 'IMG_UPpet(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'

    nameEIG_VPgde_BS = 'IMG_BeforeSegm_VPgde_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameEIG_VPmed_BS = 'IMG_BeforeSegm_VPmed_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameEIG_VPpet_BS = 'IMG_BeforeSegm_VPpet_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'

    nameSVD_VPgde_BS = 'IMG_BeforeSegm_VPgde(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_VPmed_BS = 'IMG_BeforeSegm_VPmed(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_VPpet_BS = 'IMG_BeforeSegm_VPpet(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'

    nameSVD_UPgde_BS = 'IMG_BeforeSegm_UPgde(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_UPmed_BS = 'IMG_BeforeSegm_UPmed(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    nameSVD_UPpet_BS = 'IMG_BeforeSegm_UPpet(SVD)_05'+str(i)+'pxTranspSup'+str(seuil)+'.png'
    
    ##### Reading Image #####
    Ib = mahotas.imread(pathB+nameB+str(i)+'.png')
    I = mahotas.imread(path+name+str(i)+ext)
    
    ##### Channels Images #####
    redb = Ib[:,:,0]
    greenb = Ib[:,:,1]
    blueb = Ib[:,:,2] 
    
    red = I[:,:,0]
    green = I[:,:,1]
    blue = I[:,:,2]
    
    ##### Filter white and transparent pixels #####
    sizeI = Ib.shape
    nblig = sizeI[0]
    nbcol = sizeI[1]
    
    elt_del = [(nbcol*l + c+1) - 1 for l in xrange(nblig) \
                                   for c in xrange(nbcol) if  (255 - redb[l,c])**2 + (255 - greenb[l,c])**2 + (255 - blueb[l,c])**2 < seuil]
                
    ##### Remove white and transparent pixels #####
    redb2 = np.delete(redb, elt_del)
    greenb2 = np.delete(greenb, elt_del)
    blueb2 = np.delete(blueb, elt_del)
    
    ##### Mean calcul #####
    rm = np.mean(redb2)
    rsig = np.var(redb2)
    gm = np.mean(greenb2)
    gsig = np.var(greenb2)
    bm = np.mean(blueb2)
    bsig = np.var(blueb2)
    
    print 'Image ', name+str(i)+ext, '\n'  
    print '\n', 'rm = ', rm
    print 'gm = ', gm
    print 'bm = ', bm, '\n'
    
    ##### Substract means to every value #####
    redm = np.asarray([x-rm for x in red])
    greenm = np.asarray([x-gm for x in green])
    bluem = np.asarray([x-bm for x in blue])
    
    Im = np.zeros(I.shape)
    Im[:,:,0] = redm
    Im[:,:,1] = greenm
    Im[:,:,2] = bluem
    
    ##### Image Color Processing #####
    tmp = np.reshape(Im,(2048*3072,3))
    M = np.cov(tmp.T)
    
    ##### EIG #####
    w, v = la.eig(M)
    
    v0 = v[:,0]
    v1 = v[:,1]
    v2 = v[:,2]
    
    I0 = v0[0]*redm + v0[1]*greenm + v0[2]*bluem
    I1 = v1[0]*redm + v1[1]*greenm + v1[2]*bluem
    I2 = v2[0]*redm + v2[1]*greenm + v2[2]*bluem
    
    ##### SVD #####
    U, s, V = la.svd(M)
    
    V0 = V[:,0]
    V1 = V[:,1]
    V2 = V[:,2]
    
    IV0 = V0[0]*redm + V0[1]*greenm + V0[2]*bluem
    IV1 = V1[0]*redm + V1[1]*greenm + V1[2]*bluem
    IV2 = V2[0]*redm + V2[1]*greenm + V2[2]*bluem
        
        ### Around ###
    I0A = np.around(I0)
    I1A = np.around(I1)
    I2A = np.around(I2)

    IV0A = np.around(IV0)
    IV1A = np.around(IV1)
    IV2A = np.around(IV2)
        
        ### -> uint8 ###
    I0U = I0A.astype(np.uint8)
    I1U = I1A.astype(np.uint8)
    I2U = I2A.astype(np.uint8)
        
    IV0U = IV0A.astype(np.uint8)
    IV1U = IV1A.astype(np.uint8)
    IV2U = IV2A.astype(np.uint8)
    
        ### Otsu ###
    IS0 = OtsuProprement(I0U)
    IS1 = OtsuProprement(I1U)
    IS2 = OtsuProprement(I2U)

    ISV0 = OtsuProprement(IV0U)
    ISV1 = OtsuProprement(IV1U)
    ISV2 = OtsuProprement(IV2U)
    
    ##### Saving Segmented Images #####
    ### EIG ###
    smisc.imsave(pathEIG_VPgde+nameEIG_VPgde,IS0)
    smisc.imsave(pathEIG_VPmed+nameEIG_VPmed,IS1)
    smisc.imsave(pathEIG_VPpet+nameEIG_VPpet,IS2)
    ### SVD ###
    smisc.imsave(pathSVD_VPgde+nameSVD_VPgde,ISV0)
    smisc.imsave(pathSVD_VPmed+nameSVD_VPmed,ISV1)
    smisc.imsave(pathSVD_VPpet+nameSVD_VPpet,ISV2)