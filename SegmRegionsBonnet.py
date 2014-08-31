# -*- coding: utf-8 -*-
"""
@author: amale
"""

import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import numpy as np
import mahotas
import scipy.misc as smisc

path = 'MC70/'
pathS = path+'RegionSegmentation/IMG05'
name = 'IMG_05'
ext = '.JPG'

#### Region 1 ####
rm1 = 138.
gm1 = 40.
bm1 = 48.
sigr1 = 8.6
sigg1 = 7.9
sigb1 = 7.9

#### Region 2 ####
rm2 = 176.
gm2 = 73.
bm2 = 84.
sigr2 = 8.6
sigg2 = 9.6
sigb2 = 9.2

#### Region 3 ####
rm3 = 177.
gm3 = 75.
bm3 = 85.
sigr3 = 8.5
sigg3 = 9.9
sigb3 = 9.5

#### Region 4 ####
rm4 = 95.
gm4 = 25.
bm4 = 32.
sigr4 = 8.7
sigg4 = 5.6
sigb4 = 6.3

#### Region 5 ####
rm5 = 120.
gm5 = 36.
bm5 = 44.
sigr5 = 8.4
sigg5 = 7.3
sigb5 = 7.4

#### Region 6 ####
rm6 = 178.
gm6 = 80.
bm6 = 88.
sigr6 = 7.
sigg6 = 7.8
sigb6 = 7.3

#### Region 7 ####
rm7 = 114.
gm7 = 32.
bm7 = 38.
sigr7 = 8.1
sigg7 = 6.9
sigb7 = 7.8

#### Def Function ####
def segmColor(PR,PG,PB,rm,gm,bm,sigr,sigg,sigb):
    SR = (PR - rm)**2 / sigr**2
    SG = (PG - gm)**2 / sigg**2
    SB = (PB - bm)**2 / sigb**2
    Scolor = np.empty(I.shape)
    Scolor[:,:,0] = SR
    Scolor[:,:,1] = SG
    Scolor[:,:,2] = SB
    Scolor = Scolor.astype(np.uint8)
    return Scolor
    

for i in [28, 29, 32, 33, 37, 42, 47, 52, 57, 62, 66]:

    #### Reading image ####
    I = mahotas.imread(path+name+str(i)+ext)
    IB = mahotas.imread(path+'IMG_Bonnet/IMG_Bonnet_05'+str(i)+'.png')
    
    size = np.shape(I)
    nblig = size[0]
    nbcol = size[1]    
    
    #### Extracting channels ####
    PR = I[:,:,0]
    PG = I[:,:,1]
    PB = I[:,:,2]
    
    PRB = IB[:,:,0]
    PGB = IB[:,:,1]
    PBB = IB[:,:,2]
    
    elt_del = [(nbcol*l + c+1) - 1 for l in xrange(nblig) for c in xrange(nbcol) if  IB[l,c,3] == 0]  
    PRB = np.delete(PRB, elt_del)
    PGB = np.delete(PGB, elt_del)
    PBB = np.delete(PBB, elt_del)
    
    rmB = np.mean(PRB)
    gmB = np.mean(PGB)
    bmB = np.mean(PBB)
    
    sigrB = np.var(PRB)
    siggB = np.var(PGB)
    sigbB = np.var(PBB)
    
    SB = (PRB - rmB)**2 / sigrB + (PGB - gmB)**2 / siggB + (PBB - bmB)**2 / sigbB
    
    #### Calculs criteres avec stats calculees, pour chaque region bonnet ####
    S1 = (PR - rm1)**2 / sigr1**2 + (PG - gm1)**2 / sigg1**2 + (PB - bm1)**2 / sigb1**2
        #### Pareil que S1 mais en couleur
    Scolor1 = segmColor(PR,PG,PB,rm1,gm1,bm1,sigr1,sigg1,sigb1)
    
    S2 = (PR - rm2)**2 / sigr2**2 + (PG - gm2)**2 / sigg2**2 + (PB - bm2)**2 / sigb2**2 
    Scolor2 = segmColor(PR,PG,PB,rm2,gm2,bm2,sigr2,sigg2,sigb2)
    
    S3 = (PR - rm3)**2 / sigr3**2 + (PG - gm3)**2 / sigg3**2 + (PB - bm3)**2 / sigb3**2
    Scolor3 = segmColor(PR,PG,PB,rm3,gm3,bm3,sigr3,sigg3,sigb3)
    
    S4 = (PR - rm4)**2 / sigr4**2 + (PG - gm4)**2 / sigg4**2 + (PB - bm4)**2 / sigb4**2
    Scolor4 = segmColor(PR,PG,PB,rm4,gm4,bm4,sigr4,sigg4,sigb4)
    
    S5 = (PR - rm5)**2 / sigr5**2 + (PG - gm5)**2 / sigg5**2 + (PB - bm5)**2 / sigb5**2
    Scolor5 = segmColor(PR,PG,PB,rm5,gm5,bm5,sigr5,sigg5,sigb5)
    
    S6 = (PR - rm6)**2 / sigr6**2 + (PG - gm6)**2 / sigg6**2 + (PB - bm6)**2 / sigb6**2
    Scolor6 = segmColor(PR,PG,PB,rm6,gm6,bm6,sigr6,sigg6,sigb6)
    
    S7 = (PR - rm7)**2 / sigr7**2 + (PG - gm7)**2 / sigg7**2 + (PB - bm7)**2 / sigb7**2
    Scolor7 = segmColor(PR,PG,PB,rm7,gm7,bm7,sigr7,sigg7,sigb7)
    
    #### Max de SB ####
    MB = np.amax(SB)
    
    #### Segmentation ####
    IS1 = S1 < MB
    IS2 = S2 < MB
    IS3 = S3 < MB
    IS4 = S4 < MB
    IS5 = S5 < MB
    IS6 = S6 < MB
    IS7 = S7 < MB
    
    ISU1 = 255 * IS1.astype(np.uint8)
    ISU2 = 255 * IS2.astype(np.uint8)
    ISU3 = 255 * IS3.astype(np.uint8)
    ISU4 = 255 * IS4.astype(np.uint8)
    ISU5 = 255 * IS5.astype(np.uint8)
    ISU6 = 255 * IS6.astype(np.uint8)
    ISU7 = 255 * IS7.astype(np.uint8)

    IS = IS1+IS2+IS3+IS4+IS5+IS6+IS7
    ISU = np.zeros(S1.shape, dtype=np.uint8)
    ISU[IS] = 255

    #### Saving results ####
    smisc.imsave(pathS+str(i)+'/S/S_R1_'+name+str(i)+ext,S1)
    smisc.imsave(pathS+str(i)+'/S/S_R2_'+name+str(i)+ext,S2)
    smisc.imsave(pathS+str(i)+'/S/S_R3_'+name+str(i)+ext,S3)
    smisc.imsave(pathS+str(i)+'/S/S_R4_'+name+str(i)+ext,S4)
    smisc.imsave(pathS+str(i)+'/S/S_R5_'+name+str(i)+ext,S5)
    smisc.imsave(pathS+str(i)+'/S/S_R6_'+name+str(i)+ext,S6)
    smisc.imsave(pathS+str(i)+'/S/S_R7_'+name+str(i)+ext,S7)
    
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R1_'+name+str(i)+ext,Scolor1)
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R2_'+name+str(i)+ext,Scolor2)
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R3_'+name+str(i)+ext,Scolor3)
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R4_'+name+str(i)+ext,Scolor4)
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R5_'+name+str(i)+ext,Scolor5)
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R6_'+name+str(i)+ext,Scolor6)
    smisc.imsave(pathS+str(i)+'/S/Color/Scolor_R7_'+name+str(i)+ext,Scolor7)
    
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R1_'+'MaxBonnet_'+name+str(i)+ext,ISU1)
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R2_'+'MaxBonnet_'+name+str(i)+ext,ISU2)
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R3_'+'MaxBonnet_'+name+str(i)+ext,ISU3)
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R4_'+'MaxBonnet_'+name+str(i)+ext,ISU4)
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R5_'+'MaxBonnet_'+name+str(i)+ext,ISU5)
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R6_'+'MaxBonnet_'+name+str(i)+ext,ISU6)
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_R7_'+'MaxBonnet_'+name+str(i)+ext,ISU7)
    
    smisc.imsave(pathS+str(i)+'/MaxBonnet/IS_sum_'+'MaxBonnet_'+name+str(i)+ext,IS)
#    print MB, SB
#    print 'IMG_05', str(i), '-> Checked \n'

