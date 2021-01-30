# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:00:35 2021

@author: VolkanKarakuş
"""

#lineplot,scatterplot,barplot,subplot,histogram

import pandas as pd

#csv dosyasini DataFrame'e atalim.
dataFrame = pd.read_csv('iris.csv')
columns=dataFrame.columns
info=dataFrame.info()
describe=dataFrame.describe() # numeric degerlerle ilgili max,min,mean,std gibi degerler.

#bu cicekleri ayiralim.
setosa=dataFrame[dataFrame.Species=='Iris-setosa']
versicolor=dataFrame[dataFrame.Species=='Iris-versicolor']
virginica=dataFrame[dataFrame.Species=='Iris-virginica']
#artik bu ikisini describe ile karsilastirabilirim.
print(setosa.describe())
print(versicolor.describe())


#%% matplotlib LINEPLOT
import matplotlib.pyplot as plt

#datasetteki ID'den kurtulalim, bize birsey ifade etmedigi icin.
dataFrame1=dataFrame.drop(['Id'],axis=1)

#bunu gorsellestirelim.
#dataFrame1.plot()
#plt.show() 
#bu bize bir deger vermedi aslinda. 50ID'de bir peakler var.


# describe edince farkettigimiz sey PetalLengthCm'lerin meanleri arasinda gozle gorulur farklılıklar vardı.
#daha da anlamli hale getirmek icin
plt.plot(setosa.Id,setosa.PetalLengthCm,color='red',label='setosa')
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color='green',label='versicolor')
plt.plot(virginica.Id,virginica.PetalLengthCm,color='blue',label='virginica')
plt.legend() # yukaridaki label'i koymamizi sagliyor.
plt.xlabel('ID')
plt.ylabel('PetalLengthCm')
plt.show()

#grid ve nokta ekleyelim, saydamligi degistirelim.bu parametreleri koymasak da olurdu.
dataFrame1.plot(grid=True,linestyle=':',alpha=0.8)
plt.show()
