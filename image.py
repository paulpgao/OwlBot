import numpy as np
import scipy
from scipy import ndimage
import glob
import pickle

# setting up the training set
train_set_owl = np.zeros((10, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/owlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_owl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1
y_owl = np.ones((10, 1))

train_set_nonowl = np.zeros((10, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/nonowlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_nonowl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1
y_nonowl = np.zeros((10, 1))

train_set_x = np.concatenate((train_set_owl, train_set_nonowl), axis=0)
train_set_y = np.concatenate((y_owl, y_nonowl), axis=0).T

train_set_x = (train_set_x.reshape(train_set_x.shape[0], -1)).T / 255

# training

def sigmoid(x):
    s = 1.0 / (1.0 + np.exp(-x))
    return s

def propagate(w, b, X, Y):
    m = X.shape[1]

    A = sigmoid(np.matmul(w.T, X) + b)  # compute activation
    cost = (-1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))  # compute cost

    dw = (1 / m) * np.matmul(X, (A - Y).T)
    db = (1 / m) * np.sum(A - Y)

    grads = {"dw": dw, "db": db}

    return grads, cost

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):

    costs = []

    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)

        dw = grads["dw"]
        db = grads["db"]

        w -= learning_rate * dw
        b -= learning_rate * db

        if i % 100 == 0:
            costs.append(cost)

        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    params = {"w": w, "b": b}

    grads = {"dw": dw, "db": db}

    return params, grads, costs

def predict(w, b, X):

    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)

    A = sigmoid(np.matmul(w.T, X) + b)

    for i in range(A.shape[1]):

        if A[0][i] <= 0.5:
            Y_prediction[0][i] = 0
        else:
            Y_prediction[0][i] = 1

    return Y_prediction


def model(X_train, Y_train, num_iterations=5000, learning_rate=0.5):

    w = np.zeros((np.shape(X_train)[0], 1))
    b = 0

    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost=False)

    w = parameters["w"]
    b = parameters["b"]

    Y_prediction_train = predict(w, b, X_train)

    d = {"w": w, "b": b}

    return d

d = model(train_set_x, train_set_y, num_iterations = 2000, learning_rate = 0.005)

# def predict_nonlogical(w, b, X):
#
#     m = X.shape[1]
#     w = w.reshape(X.shape[0], 1)
#
#     A = float(sigmoid(np.matmul(w.T, X) + b))
#     print (A)
#
#     return A

pred = open('pred.pckl', 'wb')
pickle.dump(d, pred)
pred.close()

# print (d)
