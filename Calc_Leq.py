import sys
import math

if __name__ == "__main__":

    print("Numero de intervalos del mismo tiempo: ")
    N = int(input())
    _Levels = []

    for i in range(0, N):
        print("Nivel Equivalente de cada Intervalo: ")
        SPL = float(input())
        _Levels.append(10.0**(0.1*SPL))

    print("\n")
    print ("Tu Nivel Equivalente Total: ")
    print("{0:0.1f}".format((10*math.log10((1/N)*(sum(_Levels))))) + " dB")
