# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:16:38 2021

@author: yusuf
"""

from tkinter import *
import logistic_regression as lr
 
root = Tk()

var = IntVar()
rbKadin = Radiobutton(root, text="Kadın", variable=var, value="1")
rbErkek = Radiobutton(root, text="Erkek", variable=var, value="0")

lblCinsiyet = Label(root, text="Cinsiyet")
#txtCinsiyet = Entry(root)

lblHGB = Label(root, text="HGB")    
txtHGB = Entry(root)

lblMCH = Label(root, text="MCH")
txtMCH = Entry(root)

lblMCHC = Label(root, text="MCHC")
txtMCHC = Entry(root)

lblMCV = Label(root, text="MCV")
txtMCV = Entry(root)

rbKadin.grid(row=0, column=1)
rbErkek.grid(row=0, columnspan=3)

lblCinsiyet.grid(row=0, column=0)
#txtCinsiyet.grid(row=0, column=1)

lblHGB.grid(row=1, column=0)
txtHGB.grid(row=1, column=1)

lblMCH.grid(row=2, column=0)
txtMCH.grid(row=2, column=1)

lblMCHC.grid(row=3, column=0)
txtMCHC.grid(row=3, column=1)

lblMCV.grid(row=4, column=0)
txtMCV.grid(row=4, column=1)

lblSonuc = Label(root, text="-")
lblSonuc.grid(row=5, column=1)


def test():
    #cinsiyet = float(txtCinsiyet.get())
    cinsiyet = float(var.get())
    hgb = float(txtHGB.get())
    mch = float(txtMCH.get())
    mchc = float(txtMCHC.get())
    mcv = float(txtMCV.get())
    sonuc = lr.logistic_regression(cinsiyet, hgb, mch, mchc, mcv)
    print(cinsiyet,hgb,mch,mchc,mcv)
    print(sonuc)
    lblSonuc.config(text="Sonuc: "+sonuc)
    
    #print("merhabalar {0} {1} {2} {3} {4}".format(cinsiyet,hgb,mch,mchc,mcv))

btnButon = Button(root,text="Gönder", padx=50, pady=5, command=test)
btnButon.grid(row=5, column=0)

root.mainloop()

