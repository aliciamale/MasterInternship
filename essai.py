#!/user/amale/home/python2.7

# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/user/amale/home/.spyder2/.temp.py
"""

import scipy.misc
import numpy as np
import scipy
import pylab
import pymorph
import mahotas
import SRM

from scipy.misc import imread
from matplotlib import pyplot
from SRM import SRM

im = imread("IMG_0533_4.JPG")

srm = SRM(im, 256)
segmented = srm.run()

pyplot.imshow(segmented/256)
pyplot.show()