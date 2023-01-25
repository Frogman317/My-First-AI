import pandas as pd

data_list = pd.read_csv("My-First-AI/Iris.csv")

# 学習データ
X = data_list[['SepalLength' , 'SepalWidth' , 'PetalLength' , 'PetalWidth']]
Y = data_list['Species']