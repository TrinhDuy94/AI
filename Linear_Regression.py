import pandas as pd
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://github.com/TrinhDuy94/AI/blob/master/Advertising.csv?raw=true"
dataframe = pd.read_csv(url)
#print(dataframe)
X = dataframe.values[: ,2]
Y = dataframe.values[: ,4]
plt.scatter(X, Y, marker='o')
plt.show()

def predict(new_radio, weight, bias):
    return weight*new_radio + bias

def cost_function(X, Y, weight, bias):
    n = len(X)
    sum_error = 0
    for i in range(n):
        sum_error += (Y[i] - (weight*X[i] + bias))**2
        
    return sum_error/n

def update_weight(X, Y, weight, bias, learning_rate):
    n = len(X)
    weight_temp = 0.0
    bias_temp =0.0
    for i in range(n):
        weight_temp += -2*X[i]*(Y[i] - (X[i]*weight +bias))
        bias_temp += -2*(Y[i] - (X[i]*weight +bias))
    weight -= (weight_temp/n)*learning_rate
    bias -= (bias/n)*learning_rate
    
    return weight, bias

def train(X, Y, weight, bias, learning_rate, iter):
    cost_his = []
    for i in range(iter):
        weight, bias = update_weight(X, Y, weight, bias, learning_rate)
        cost = cost_function(X, Y, weight, bias)
        cost_his.append(cost)
    
    return weight, bias, cost_his

weight, bias, cost = train(X, Y, 0.03, 0.0014, 0.001, 60)
print("Ket Qua: ")
print(weight)
print(bias)
print(cost)
print("Gia Tri Du Doan: ")
print(predict(19, weight, bias))

#solanlap = [i for i in range(60)]
#plt.plot(solanlap,cost)
#plt.show()