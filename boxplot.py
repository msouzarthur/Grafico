import matplotlib.pyplot as plt
import random
vetor = []
for i in range(20):
    num = random.randint(0,4200)
    vetor.append(num)
plt.boxplot(vetor)
plt.title('boxplot')
plt.show() 