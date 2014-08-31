import sys
sys.path.append('/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL')

import numpy
import scipy.misc as smisc
import mahotas
#from matplotlib import pyplot
import SRM
from SRM import SRM

im = mahotas.imread('MC70/IMG_0528.JPG')

srm = SRM(im, 256)
segmented = srm.run()

smisc.imsave('IMG_SRM_0528.png',segmented/256)
#pyplot.imshow(segmented/256)
#pyplot.show()