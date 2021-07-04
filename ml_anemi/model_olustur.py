# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:16:38 2021

@author: yusuf
"""

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

veri = pd.read_excel("veri.xlsx")

X = veri.iloc[:,1:6]
y = veri.iloc[:,6]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.transform(X_test)

model = LogisticRegression(random_state=0)
model.fit(X_train, y_train)

pickle.dump(model,open('model.sav', 'wb'))
