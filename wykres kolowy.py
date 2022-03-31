import matplotlib.pyplot as plt 
import numpy as np

tak=np.array([206,196,118,92,83,39])
lista=["SPD","CDU/CSU","GREENS","FPD","AFD","Left Party"]

plt.pie(tak, labels=lista, startangle = 100,autopct='%.2f%%')
plt.show()