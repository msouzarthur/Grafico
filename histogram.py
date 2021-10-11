import matplotlib.pyplot as plt
a = (0, 1, 1, 1, 2, 3, 7, 7, 23)

#hist é um gráfico linear
plt.hist(a)
#plt.hist(termo, agrupamento)
#plt.hist(a, bins=5) - usa 5 grupos
plt.show()