# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:16:38 2021

@author: yusuf
"""

import numpy as np
import pickle

def logistic_regression(cinsiyet,hgb,mch,mchc,mcv):
    
    model = pickle.load(open("model.sav", 'rb'))
    yeni_veri = np.array([[cinsiyet,hgb,mch,mchc,mcv]])
    yeni_veri_tahmin = model.predict(yeni_veri)
    
    if(yeni_veri_tahmin==1):
        print(yeni_veri_tahmin)
        return "anemi"
    if(yeni_veri_tahmin==0):
        print(yeni_veri_tahmin)
        return "anemi yok"
    else:
        print("hata")
        return "hata!"
