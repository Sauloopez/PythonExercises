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
        k1=Data.calculate_k_prd()
        k2=Data.calculate_k()
        pob=7821 * mt.exp(k1*y)
        print(pob, k1)
        pob=7821 * mt.exp(k2*y)
        print(pob, k2)

    def calculate_k():
        with open("data.json", "r") as file:
            data = js.load(file)
        years=[]
        for y in data:
            years.append(int(y))
        
        log_values = np.array([mt.log(int(data[str(year)]), mt.e) for year in years])

        slope, intercept = np.polyfit(years, log_values, 1)

        return slope
    
    def calculate_k_prd():
        with open("data.json", "r") as file:
            data = js.load(file)
        years=[]
        poblacion=[]
        for y in data:
            poblacion.append(int(data[y]))
            years.append(int(y))
        for i in poblacion:
            if len(poblacion) != poblacion.index(i) and poblacion.index(i) > 0:
                k = (mt.log(i / poblacion[poblacion.index(i)-1])) / (years[poblacion.index(i)]-years[poblacion.index(i)-1])
                     
        return k

        

#years=Data()
#years.input_content()
Data.model(3)

