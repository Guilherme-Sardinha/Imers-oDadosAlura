#Desafio1: Proporção de inscritos por idade.

import pandas as pd #importa a biblioteca pandas e define um apelido

import matplotlib.pyplot as plt #importa a biblioteca Matplot e define um apelido

#busca a fonte de dados
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#lê o arquivo csv e define este valor para a variavel dados
dados = pd.read_csv(fonte)

#conta a quantidade de idades, ou seja, o tamanho total de nossa amostra
numero = len(dados["NU_IDADE"])

#Divide a quantidade de participantes de cada idade pelo total e multiplica por 100 para apresentar o número em porcentagem
proporcao = ((dados["NU_IDADE"].value_counts().sort_index()/numero)*100)

#Mostra em tela o valor da proporção em tabela
print(proporcao)

#Gera um grafico de linha para apresentar a proporção
proporcao.plot()
#Adiciona um titulo ao grafico
plt.title('Proporção por idade')
#Coloca o nome para o eixo X
plt.xlabel('Idade')
#Coloca o nome para o eixo Y
plt.ylabel('Proporção')
#Adiciona uma legenda no melhor lugar
plt.legend(loc='best')
#gera em tela o gráfico
plt.show()