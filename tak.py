import numpy as np
from numpy import random
aw = int(input("Podaj wielkosc dla macierzy A: \n"))
ak = int(input("Podaj wielkosc dla macierzy A: \n"))
bw = int(input("Podaj wielkosc dla macierzy A: \n"))
bk = int(input("Podaj wielkosc dla macierzy B: \n"))

if ak != bw:
    print("wykonanie działania jest niemozliwe")
    pass
else:
    tab1 = np.random.randint(1000,size=(aw,ak))
    tab2 = np.random.randint(1000,size=(bw, bk))

    print("pierwsza macierz:")
    print(tab1)
    print("druga macierz:")
    print(tab2)
    print("dodawanie macierzy:")
    print(tab1 + tab2)
    print("mnozenie macierzy")
    print(tab1 * tab2)

