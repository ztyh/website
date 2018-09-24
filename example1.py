import pandas as pd
df_sample =pd.DataFrame(
             [["day1","day2","day1","day2","day1","day2"],
              ["A","B","A","B","C","C"],
              [100,150,200,150,100,50],
              [120,160,100,180,110,80]] ).T
df_sample.columns = ["day_no","class","score1","score2"]
df_sample.index   = ["alice","bob","chris","dave","evan","fred"]
print(df_sample)
#help(pd.read_csv)
M=pd.read_csv("matrix.csv",header=None)
print(len(M.index))
# for lab use shape
M[0][0]
M.iloc[1:3,1:3]
M.iloc[1:3,1]
M.iloc[1:3,]
M.iloc[1:3,].mean(0)
M.iloc[1:3,].mean(1)
from sklearn.datasets import load_iris
iris = load_iris()
data=pd.DataFrame(iris.data, columns=iris.feature_names)
# 0: 'setosa', 1: 'versicolor', 2: 'virginica'
data.head(2)
iris.target
vriginica=data[iris.target==2]
data.columns
subset=data[data['petal width (cm)']>2]
concat=pd.concat([vriginica,subset])
concat.drop_duplicates
