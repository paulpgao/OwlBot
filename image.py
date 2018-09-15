from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy
from scipy import ndimage
import glob

train_set_owl = np.zeros((120, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/owlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_owl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1
y_owl = np.ones((120, 1))

train_set_nonowl = np.zeros((100, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/nonowlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_nonowl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1
y_nonowl = np.zeros((100, 1))

train_set_x = np.concatenate((train_set_owl, train_set_nonowl), axis=0)
train_set_y = np.concatenate((y_owl, y_nonowl), axis=0).T

print (train_set_y)
