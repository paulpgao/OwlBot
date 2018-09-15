from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy
from scipy import ndimage
import glob


# imagelist = [f for f in listdir("F:/Paul Gao/Documents/randombot/owlimages") if isfile(join("F:/Paul Gao/Documents/randombot/owlimages", f))]

# my_image = imagelist[0]  # change this to the name of your image file
## END CODE HERE ##

# We preprocess the image to fit your algorithm.
# image = np.array(ndimage.imread("F:/Paul Gao/Documents/randombot/owlimages", flatten=False))
# my_image = scipy.misc.imresize(image, size=(64, 64)).reshape((1, 64*64*3)).T
#
# print (my_image)

train_set_owl = np.zeros((120, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/owlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_owl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1

train_set_nonowl = np.zeros((100, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/nonowlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_nonowl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1

train_set = np.concatenate((train_set_owl, train_set_nonowl), axis=0)

print(np.shape(train_set))



