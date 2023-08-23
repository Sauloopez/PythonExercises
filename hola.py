import numpy as np
import statistics as st
import matplotlib.pyplot as plt


class Clase :
    
    def __init__(self):
        self.m=1
        self.f=2
        m=1
        f=2
        self.estaturas = [1.85, 1.80, 1.83, 1.65, 1.69, 1.82, 1.69, 1.69, 1.68, 1.73, 1.54, 1.71, 1.93, 1.55, 1.66, 1.78, 1.85, 1.90, 1.61, 1.79]
        self.edades = [22, 20, 20, 22, 21, 20, 19, 20, 22, 30, 28, 29 ,25, 38, 21, 24, 26, 27, 27, 31]
        self.pesos = [115, 60, 63, 60, 55, 80, 76, 60, 75, 64, 72, 78, 88, 54, 66, 74, 80, 92, 74, 66]
        self.sexos=[m, m, m, m , m, m, f, f, f, m, f, f, m, f, m, f, f, m, f, f]
    def getMedias(self):
        self.medias=[np.mean(self.estaturas), np.mean(self.edades), np.mean(self.pesos), np.mean(self.sexos)]
        print("Media de estaturas: ",np.mean(self.estaturas))
        print("Media de edades: ",np.mean(self.edades))
        print("Media de pesos: ",np.mean(self.pesos))
        mediasexos=np.mean(self.sexos)
        if mediasexos != 1 or mediasexos!= 2:
            mediasexos="hay la misma cantidad de integrantes de ambos sexos"
        print("Media de sexos: ",mediasexos, ": ", np.mean(self.sexos))
        return self.medias
    
    def getModas(self):
        print("Moda de estaturas", self.moda(self.estaturas))
        print("Moda de edades", self.moda(self.edades))
        print("Moda de pesos", self.moda(self.pesos))
        modasexos =self.moda(self.sexos) 
        if modasexos ==self.m:
            modasexos="masculino"
        elif modasexos == self.f:
            modasexos="femenino"
        print("Moda de sexos", modasexos)

    def getMedianas(self):
        print("Mediana de estaturas", self.mediana(self.estaturas))
        print("Mediana de edades", self.mediana(self.edades))
        print("Mediana de pesos", self.mediana(self.pesos))
        modasexos =self.mediana(self.sexos) 
        if modasexos ==self.m:
            modasexos="masculino"
        elif modasexos == self.f:
            modasexos="femenino"
        else:
            modasexos ="Hay la misma cantidad de integrantes de ambos sexos"
        print("Moda de sexos: ", modasexos)

    def getDesviacionEstandar(self):
        print("Desv Estandar de estaturas", self.desvEstandar(self.estaturas))
        print("Desv Estandar de edades", self.desvEstandar(self.edades))
        print("Desv Estandar de pesos", self.desvEstandar(self.pesos))
        modasexos =self.mediana(self.sexos)
        print("Desv Estandar de sexos: ", modasexos)

    def desvEstandar(self, array):
        return np.std(array).round(4)
    def moda(self, array):
        return st.mode(array)
    
    def mediana(self, array):
        return st.median(array)
    def graficar(self):
        fig, ax = plt.subplots()
        f=self.sexos.count(self.f)
        m=self.sexos.count(self.m)
        pesosM=[]
        estaturasM=[]
        pesosF=[]
        estaturasF=[]
        for i in range(len(self.sexos)):
            if(self.sexos[i] == self.m):
                pesosM.append(self.pesos[i])
                estaturasM.append(self.estaturas[i])
            else:
                pesosF.append(self.pesos[i])
                estaturasF.append(self.estaturas[i])
        mediaPesosM=np.mean(pesosM)
        mediaPesosF=np.mean(pesosF)
        sticks=['masculino', 'femenino']
        n = len(sticks)
        x = np.arange(n)
        width = 0.25
        ax.bar(x-width, [np.mean(estaturasM)*10, np.mean(estaturasF)*10], width=width ,label='Media de estaturas')
        ax.bar(x, [m, f], width=width, label='Sexo')
        ax.bar(x+width, [mediaPesosM, mediaPesosF], width=width, label='Media de Peso')
        ax.set_ylabel('Nro_Estudiantes/Estatura(dm)/Peso(Kg)')
        
        ax.grid(axis='y', color='gray', linestyle='dashed')
        plt.legend(loc='best')
        plt.xticks(x, sticks)
        plt.show()

    def comportamientoEdad(self):
        fig, ax = plt.subplots()
        sticks=[]
        i=0
        while i !=20:
            i+=1
            sticks.append(i)
        
        ax.set_ylabel('Edad(años)')    
        ax.plot(sticks, self.edades)
        plt.xticks(sticks)
        plt.show()
    def comportamientoMasa(self):
        fig, ax = plt.subplots()
        sticks=[]
        i=0
        while i !=20:
            i+=1
            sticks.append(i)
        
        ax.set_ylabel('Masa(Kg)')    
        ax.plot(sticks, self.pesos)
        plt.xticks(sticks)
        plt.show()
    def comportamientoEst(self):
        fig, ax = plt.subplots()
        sticks=[]
        i=0
        while i !=20:
            i+=1
            sticks.append(i)
        
        ax.set_ylabel('Estatura(Mts)')    
        ax.plot(sticks, self.estaturas)
        plt.xticks(sticks)
        plt.show()
        
    def comportamientoGen(self):
        fig, ax = plt.subplots()
        ax.set_ylabel('Nro. Personas')
        ax.bar(['masculino', 'femenino'], [self.sexos.count(self.m), self.sexos.count(self.f)])
        plt.show()
    def masas(self):
        fig, ax = plt.subplots()
        pesosM=[]
        posM=[]
        pesosF=[]
        posF=[]
        for i in range(len(self.sexos)):
            if(self.sexos[i] == self.m):
                pesosM.append(self.pesos[i])
                posM.append(i)
            else:
                pesosF.append(self.pesos[i])
                posF.append(i)
        sticks=[]
        i=0
        while i !=10:
            i+=1
            sticks.append(i)
        ax.plot(sticks, pesosM, label='masas-masculino')
        ax.plot(sticks, pesosF, label='masas-femenino')
        ax.legend(loc ='best')
        ax.set_ylabel('Masa(kg)')
        ax.set_xticks(sticks)
        
        plt.show()

    def masasmedias(self):
        fig, ax = plt.subplots()
        pesosM=[]
        pesosF=[]
        for i in range(len(self.sexos)):
            if(self.sexos[i] == self.m):
                pesosM.append(self.pesos[i])
            else:
                pesosF.append(self.pesos[i])
        print(st.mean(pesosM), st.mean(pesosF))
        ax.bar(['masculino'], [st.mean(pesosM)], label='masas-masculino')
        ax.bar(['femenino'], [st.mean(pesosF)], label='masas-femenino')
        ax.legend(loc ='best')
        ax.set_ylabel('Masa(kg)')
        
        plt.show()

                

a=Clase()
print("-----------------Medias------------------")
Clase.getMedias(a)
print("-----------------Modas-------------------")
Clase.getModas(a)
print("-----------------Medianas-------------------")
Clase.getMedianas(a)
print("-----------------Medianas-------------------")
Clase.getDesviacionEstandar(a)

print("-----------------Analisis-------------------")
#Clase.graficar(a, a.edades)

Clase.masasmedias(a)
