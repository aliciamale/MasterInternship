import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import numpy as np
from numpy import linalg as la
import mahotas
import scipy.misc as smisc

path = 'MC70/'
name = 'IMG_05'
ext = '.JPG'

for i in [28, 29, 32, 33, 37, 42, 47, 52, 57, 62, 66]:
    
    #### Reading image ####
    I = mahotas.imread(path+name+str(i)+ext)
    
    size = np.shape(I)
    nblig = size[0]
    nbcol = size[1]
    
    #### Extracting channels ####
    PR = I[:,:,0]
    PG = I[:,:,1]
    PB = I[:,:,2]
    
    ##### Image Color Processing #####
    tmp = np.reshape(I,(2048*3072,3))
    M = np.cov(tmp.T)
    
    w, v = la.eig(M)
    v0 = v[:,0]
    v1 = v[:,1]
    v2 = v[:,2]
    
    I0 = v0[0]*PR + v0[1]*PG + v0[2]*PB
    I1 = v1[0]*PR + v1[1]*PG + v1[2]*PB
    I2 = v2[0]*PR + v2[1]*PG + v2[2]*PB
    
    I0A = np.around(I0)
    I1A = np.around(I1)
    I2A = np.around(I2)
    
    I0U = I0A.astype(np.uint8)
    I1U = I1A.astype(np.uint8)
    I2U = I2A.astype(np.uint8)
    
    smisc.imsave('IMG_eig_codebrut0_05'+str(i)+'.png',I0U)
    smisc.imsave('IMG_eig_codebrut1_05'+str(i)+'.png',I1U)
    smisc.imsave('IMG_eig_codebrut2_05'+str(i)+'.png',I2U)