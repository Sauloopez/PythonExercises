import json as js
import math as mt
import matplotlib.pyplot as pt
import numpy as np


class Data:
    def __init__(self):
        self.years=[]
        years= int(input('Digita los años: '))
        count=1900
        years+=count
        while count <= years:
            self.years.append(count)
            count+=10
            print(count)

    def input_content(self):
        self.cant=[]
        self.data={}
        file=open("data.json", "w")
        for f in self.years:
            self.data.setdefault(f,int(input(f'cant en año {f}: ')))
        js.dump(self.data, file)
    def model(y):
        k1=mt.log(7821/1650)/y
        k2=Data.calculate_k()
        pob=1650 * mt.exp(k1*y)
        print(pob, k1)
        pob=1650 * mt.exp(k2*y)
        print(pob, k2)

    def calculate_k():
        with open("data.json", "r") as file:
            data = js.load(file)
        years=[]
        for y in data:
            years.append(int(y))
        
        # Transforma los datos usando el logaritmo natural
        log_values = np.array([mt.log(int(data[str(year)]), mt.e) for year in years])

        # Ajusta una regresión lineal a los datos transformados
        slope, intercept = np.polyfit(years, log_values, 1)

        # La pendiente (slope) es constante k
        return slope

        

#years=Data()
#years.input_content()
Data.model(123)

