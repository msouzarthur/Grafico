import matplotlib.pyplot as plt
#crescimento da população brasileira 1980 - 2016
#ler arquivo
#csv : ano;valor
dados = open('populacao_brasileira.csv').readlines()
year = [] #anos
pop = [] #populacao
for i in range(len(dados)):
    if i!=0: #ignora a primeira linha (sem dados)
        #separo a linha pelo ; -> gera um vetor de duas strings
        linha = dados[i].split(';')
        #string 1 é o ano
        year.append(int(linha[0]))
        #string 2 é a população
        pop.append(int(linha[1]))

plt.plot(year,pop, color='k', linestyle='--')
plt.bar(year,pop, color='#e4e4e4')
plt.title('crescimento da população brasileira 1980 - 2016')
plt.ylabel('população - 100 milhões')
plt.xlabel('ano')
plt.show()
#plt.savefig('população.png',dpi=400)