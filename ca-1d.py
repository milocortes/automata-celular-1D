import sys
import matplotlib.pyplot as plt
import numpy as np

## Definimos algunos parámetros
columnas = 1001
regla = int(sys.argv[1])
iteraciones = int(sys.argv[2])


## Definimos la condición inicial
condicion_inicial=[0]*columnas
condicion_inicial[int((columnas-1)/2)]=1

class CellularAutomata:
    def __init__(self,regla, iteraciones, condicion_inicial):
        self.estados = ['111','110','101','100','011','010','001','000']
        self.regla_binario = f'{regla:08b}'
        self.reglas_dic = dict(zip(self.estados, [int(x) for x in self.regla_binario]))
        self.iteraciones = iteraciones
        self.matriz_ca = [condicion_inicial]

    def transicion(self,arreglo):

        arreglo_salida = []

        for i in range(len(arreglo)):
            anterior = i - 1
            posterior = i + 2

            vecindad = ''

            for x in range(anterior,posterior):
                if x != len(arreglo):
                    vecindad+=str(arreglo[x])
                else :
                    vecindad+=str(arreglo[0])

            arreglo_salida.append(self.reglas_dic[vecindad])

        return arreglo_salida

    def ejecucion(self):
        for x in range(self.iteraciones):
            self.matriz_ca.append(self.transicion(self.matriz_ca[x]))

    def imprime_ejecucion(self):
        for x in self.matriz_ca:
            for y in x:
                if y==0:
                    print(" ", end='')
                else:
                    print("*",end ='')
            print("")

CA=CellularAutomata(regla,iteraciones, condicion_inicial)

CA.ejecucion()
#CA.imprime_ejecucion()


# Hacemos el grid
nrows, ncols = iteraciones,columnas
image = np.array(CA.matriz_ca)
row_labels = range(nrows)
plt.matshow(image)
plt.show()
