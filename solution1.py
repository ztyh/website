import pandas as pd
df_sample =pd.DataFrame(
             [["No","Yes","No","Yes","No"],
              ["Sbarro","Panda","Big Bowl","Subway","McDonalds"],
              [5,8,10,6,5],
              [8,8,7,9,6]] ).T
df_sample.columns = ["class","lunch","budget","sleep"]
df_sample.index   = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
print(df_sample)
#help(pd.read_csv)
M=pd.read_csv("matrix.csv",header=None)
print(M.shape)
print(M.mean(0)) # column means
print(M.mean(1)) # row means
from sklearn.datasets import load_iris
iris = load_iris()
data=pd.DataFrame(iris.data, columns=iris.feature_names)
# 0: 'setosa', 1: 'versicolor', 2: 'virginica'
data.head(2)
versicolor=data[iris.target==1]
print(versicolor['petal length (cm)'].mean())
subset=data[(data['sepal length (cm)']>4.5)&(data['sepal length (cm)']<6)]
subset
concat=pd.concat([versicolor,subset])
concat.drop_duplicates
