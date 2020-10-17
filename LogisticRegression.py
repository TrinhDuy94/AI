<<<<<<< HEAD
<<<<<<< HEAD
# Hoi quy Logistic
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

plt.scatter(true_x,true_y,marker="o",c="b")
plt.scatter(false_x,false_y,marker="s",c="r")
plt.show()
#def sigmoid(z):
=======
# Hoi quy Logistic
>>>>>>> origin/master
=======
# Hoi quy Logistic
>>>>>>> origin/master
