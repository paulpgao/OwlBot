import numpy as np
import scipy
from scipy import ndimage
import glob
import pickle

# setting up the training set
train_set_owl = np.zeros((120, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/owlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    train_set_owl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1
y_owl = np.ones((120, 1))

train_set_nonowl = np.zeros((194, 64, 64, 3))
i = 0
for img in glob.glob("F:/Paul Gao/Documents/randombot/nonowlimages/*.jpg"):
    image = np.array(ndimage.imread(img, flatten=False))
    #print (i)
    train_set_nonowl[i] = scipy.misc.imresize(image, size=(64, 64))
    i += 1
y_nonowl = np.zeros((194, 1))

train_set_x_u = np.concatenate((train_set_owl, train_set_nonowl), axis=0)
# print (np.shape(train_set_x))
train_set_y_u = np.concatenate((y_owl, y_nonowl), axis=0)
# print (np.shape(train_set_y))

# training

def sigmoid(x):
    s = 1.0 / (1.0 + np.exp(-x))
    return s

def propagate(w, b, X, Y):
    m = X.shape[1]
    A = sigmoid(np.matmul(w.T, X) + b)
    cost = (-1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    dw = (1 / m) * np.matmul(X, (A - Y).T)
    db = (1 / m) * np.sum(A - Y)
    grads = {"dw": dw, "db": db}
    return grads, cost

def optimize(w, b, X, Y, num_iterations, learning_rate):
    costs = []
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        w -= learning_rate * dw
        b -= learning_rate * db
        if i % 100 == 0:
            costs.append(cost)
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

def model(X_train, Y_train, X_test, Y_test, num_iterations, learning_rate):
    w = np.zeros((np.shape(X_train)[0], 1))
    b = 0
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate)
    w = parameters["w"]
    b = parameters["b"]
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)
    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))
    return {"w": w,"b": b, "a" : 100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100}

# def find_best(par_list, train_set_x_u, train_set_y_u):
#     max_accuracy = 0
#     for i in range(10):
#         for n in par_list:
#             randomize = np.arange(len(train_set_x_u))
#             np.random.shuffle(randomize)
#             train_set_x = train_set_x_u[randomize]
#             train_set_y = train_set_y_u[randomize]
#             test_set_x = train_set_x[0:n]
#             test_set_y = train_set_y[0:n].T
#             train_set_x = train_set_x[n:]
#             train_set_y = train_set_y[n:].T
#             train_set_x = (train_set_x.reshape(train_set_x.shape[0], -1)).T / 255
#             test_set_x = (test_set_x.reshape(test_set_x.shape[0], -1)).T / 255
#             d = model(train_set_x, train_set_y, test_set_x, test_set_y, 2000, 0.005)
#             if max_accuracy < d['a']:
#                 max_accuracy = d['a']
#                 best_model = d
#     return (best_model, max_accuracy)
# d = find_best([31, 62, 93], train_set_x_u, train_set_y_u)[0]
# print (d)

randomize = np.arange(len(train_set_x_u))
np.random.shuffle(randomize)
train_set_x = train_set_x_u[randomize]
train_set_y = train_set_y_u[randomize]
n = 62
test_set_x = train_set_x[0:n]
test_set_y = train_set_y[0:n].T
train_set_x = train_set_x[n:]
train_set_y = train_set_y[n:].T
train_set_x = (train_set_x.reshape(train_set_x.shape[0], -1)).T / 255
test_set_x = (test_set_x.reshape(test_set_x.shape[0], -1)).T / 255

d = model(train_set_x, train_set_y, test_set_x, test_set_y, 2000, 0.005)

def predict_nonlogical(w, b, X):
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(np.matmul(w.T, X) + b)
    #print (A)
    return A

pred = open('pred.pckl', 'wb')
pickle.dump(d, pred)
pred.close()


