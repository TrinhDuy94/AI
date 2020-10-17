import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("https://github.com/TrinhDuy94/AI/blob/master/data_classification.csv?raw=true",header=None)

print(data.values)

true_x=[]
true_y=[]
false_x=[]
false_y=[]

for item in data.values:
    if item[2] == 1.:
        true_x.append(item[0])
        true_y.append(item[1])
    else:
        false_x.append(item[0])
        false_y.append(item[1])

#plt.scatter(true_x,true_y,marker="o",c="b")
#plt.scatter(false_x,false_y,marker="s",c="r")
#plt.show()
def sigmoid(z):
    return 1.0 / (1+np.exp(-z))

def phanchia(p):
    if p >= 0.5:
        return 1
    else:
        return 0

def predict(features, weights):
    z = np .dot(features, weights)
    return sigmoid(z)

def cost_function(features, labels, weights):
    n = len(labels)
    predictions = predict(features, weights)
    cost_class1 = -lables*np.log(predictons)
    cost_class2 = -np.log(1 - predictions)
    cost = cost_class1 + cost_class2
    return cost.sum()/n

def update_weight(features, labels, weights, learning_rate):
    n = len(lables)
    predictions = predict(features, weights)
    gd = np.dot(features.T, (predictions - labels))
    gd = gd/n
    gd = gd*learning_rate
    weights = weights - gd
    return weights