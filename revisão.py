'''
versão abreviada -> plt.plot(eixo, '123')
1-> marcador
2-> linha
3-> cor

Marcadores
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
plt.plot(x,marker=' ')

Tamanho do marker - s
plt.plot(eixo, markert=' ', s=int)

cor do marker - mec
plt.plot(eixo, markert=' ', s=int, mec='cor')

borda do marker - mfc
plt.plot(eixo, markert=' ', s=int, mec='cor', mfc='cor')

----------------------------------------
Linhas
tipos de linha - linestyle
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
plt.plot(eixo, eixo, linestyle=' ')

tamanho da linha - linewidth
-----------------------------------------
Cores (ou alfanumerico)
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
'''
import matplotlib.pyplot as plt
x = [1,3,5,7,9]
y = [2,3,7,1,0]
x1 = [2,4,6,8,10]
y1 = [5,1,3,7,4] 
'''
#Gráfico com reta
#eixo x
x = [1,2,3,4,5] 
#eixo y
y = [2,3,7,1,0]
#título
plt.title('Meu primeiro gráfico')
#legenda eixo x
plt.xlabel('Eixo X')
#legenda eixo y
plt.ylabel('Eixo Y')
#plot do gráfico
plt.plot(x,y)
#exibição
plt.show()

#Gráfico com barras
#y representa a altura das barras
titulo = 'Gráfico de barras'
eixox = 'Eixo x'
eixoy = 'Eixo y'
#título
plt.title(titulo)
#legenda eixo x
plt.xlabel(eixox)
#legenda eixo y
plt.ylabel(eixoy)
#plot do gráfico
plt.bar(x,y)
#exibição
plt.show()

#Gráfico com barras visualizar 2
#título e legendas
titulo = 'Gráfico de barras'
eixox = 'Eixo x'
eixoy = 'Eixo y'
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
#
#plot do gráfico
#label -> conteúdo da legenda (quadradinho explicando)
plt.bar(x1, y1, label="Grupo 1")
plt.bar(x, y, label="Grupo 2")
#gera o quadradinho e fixa ele 
plt.legend(loc='upper left')
#exibição
plt.show()
'''

#gráfico de pontos ligado por linhas
#personalizar o tamanho dos marker
z = [100,150,40,260,600]
titulo = 'Scatterplot: gráfico de dispersão'
eixox = 'Eixo x'
eixoy = 'Eixo y'
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#x = [1,3,5,7,9]
#y = [2,3,7,1,0]
#linha
plt.plot(x,y, linestyle='--', color='#000000')
#pontos
plt.scatter(x,y,label='meus pontos',color='k',marker='D', s=z)
plt.show()

#salvar gráfico
#dpi dita a  qualidade, mais melhor
#plt.savefig('figura1.pdf')
#plt.savefig('figura1.png',dpi=300)