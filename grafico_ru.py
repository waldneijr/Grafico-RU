# Permite o uso da biblioteca matplotlib
import matplotlib.pyplot as plt

# Salva os 3 últimos dígitos do RU em variáveis
a = 3
b = 5
c = 6
# Cria uma lista com os possíveis valores de X
x = [5, 7, 9]
# Cria uma lista de equações (onde, no gráfico, será exibido apenas o resultado) envolvendo os números do RU e os 3 possíveis valores de X
y = [a * x[0] + x[0] * b - c, a * x[1] + x[1] * b - c, a * x[2] + x[2] * b - c]
# Nomeia o eixo X
plt.xlabel('Variáveis X')
# Nomeia o eixo Y
plt.ylabel('Resultados da equação')
# Cria um gráfico de pontos relacionando as variáveis X e Y, adiciona uma legenda e muda a cor dos pontos do gráfico para vermelho
plt.scatter(x, y, label = 'Resultado da equação de acordo com a variável X', color='red')
# Mostra a legenda no gráfico
plt.legend()
# Mostra o gráfico
plt.show()