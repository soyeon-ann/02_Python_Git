import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data =  pd.read_csv('./data/1_pima.csv')
print(data)

X = array[:,0:8]
print(X, "\nX shpae is ", X.shape)
print("-----------------------")
Y = array[:,8]
print(Y, ''\nY shpae is ", Y.shape)

MinMaxScaler