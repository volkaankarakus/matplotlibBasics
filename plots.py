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

#%% SCATTER PLOT (daha cok iki tane feature karsilastirmak icin kullanilir.)
setosa=dataFrame[dataFrame.Species=='Iris-setosa']
versicolor=dataFrame[dataFrame.Species=='Iris-versicolor']
virginica=dataFrame[dataFrame.Species=='Iris-virginica']

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color='red',label='setosa')
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color='green',label='versicolor')
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color='blue',label='virginica')
plt.legend()
plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')
plt.title('Scatter Plot')
plt.show()

# goruldugu uzere setosa'yi rahatlikla digerlerinden bu featurelari kullanarak ayirabiliyoruz.

#%% HISTOGRAM
plt.hist(setosa.PetalLengthCm,bins=20) #bins degerini degistire degistire dene optimuma bak.
plt.xlabel('PetalLengthCm')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()

#%% BAR PLOT
import numpy as np

x=np.array([1,2,3,4,5,6])
y=x*2+5

plt.bar(x,y)
plt.title('Bar Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#%% SUBPLOT
#otomatic subplot
dataFrame1.plot(grid=True,alpha=0.9,subplots=True)
plt.show()

#manuel subplot
setosa=dataFrame[dataFrame.Species=='Iris-setosa']
versicolor=dataFrame[dataFrame.Species=='Iris-versicolor']
virginica=dataFrame[dataFrame.Species=='Iris-virginica']

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color='red',label='setosa')
plt.ylabel('Setosa-PetalLengthCm')
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color='green',label='versicolor')
plt.ylabel('versicolor-PetalLengthCm')
plt.show()
