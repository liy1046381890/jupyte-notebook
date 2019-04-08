"""
PassengerId 乘客id（int）
Survived  存活（0，1）
Pclass 票类别（1，2，3）
Name 不作考虑
Sex 性别（male，female）
Age 年龄（float）缺省值按照Sex划分（平均，中位数，(max-min)/2+min ...)补全
SibSp 平辈（int）
Parch 长辈晚辈 （int）
Ticket 票号（str）
Fare 票价（float）
Cbin 缺失严重不作考虑/根据船票粗略判断
Embarked 登船港口（C，Q，S）
"""

# 特征  量纲 (x-min)/(max-min)
# One-hot Encoding 独热编码
# 离群点？

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('titanic/train.csv')
test = pd.read_csv('titanic/test.csv')
print(test.loc[test.Fare.isnull()].Ticket)#3701
lst = [str(i) for i in range(3000, 6000)]
print(test.loc[test.Ticket.isin(lst)].Ticket)#3410,3470
print(test.loc[test.Ticket.isin(lst)].Fare)#8.7125,7.8875
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# Embarked_C = train.Pclass[train.Embarked == 'C'].value_counts()
# Embarked_Q = train.Pclass[train.Embarked == 'Q'].value_counts()
# Embarked_S = train.Pclass[train.Embarked == 'S'].value_counts()
# Pclass_df = pd.DataFrame({'C': Embarked_C, 'Q': Embarked_Q, 'S': Embarked_S})
# Pclass_df.plot(kind='bar', stacked=True)
# plt.title('不同票等乘客的登船港口分布')
# plt.xlabel('票等')
# plt.ylabel('乘客上传港口')
# plt.show()
# print(train.loc[train.Pclass.isin([1])].Embarked.mode()[0])
print(train.loc[train.Sex.isin(['female'])].Age.mean())
