#importa a biblioteca
import matplotlib.pyplot as plt
#define os dados
year=[1950,1978,1990,2010]
pop = [2.519,3.698,5.263,6.972]

#adicionar mais informações
year = [1800, 1850, 1900] + year
pop = [1.0,1.262,1.650] + pop
#gera o grafico
#grafico com linha
#plt.plot(year,pop)
#grafico com ponto
#plt.scatter(year,pop)

plt.plot(year,pop)
plt.xlabel('year')
plt.ylabel('population')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

plt.title('World Population')

#exibe o grafico
plt.show()