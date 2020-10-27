#conectando o python ao SQL
import pyodbc

def retornar_conexao_sql():
    server = "DESKTOP-NTJV46D"
    database = "ENEM_2019"
    #username = "aula_mongodb"
    #password = "abc123"
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)

    return conexao.cursor()

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#Traz a uma amostra aleatória dos dados do Enem
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#Pede para o pandas ler o arquivo CSV fruto de parte dos dados do Enem
dados = pd.read_csv(fonte)

provas = ['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_REDACAO']

dados[provas].sum(axis=1)

dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)


nzero = dados.query('NU_NOTA_TOTAL!=0')

#gera o histograma para as notas diferentes de zero e coloca no eixo x o valor total das notas
sns.histplot(nzero, x = "NU_NOTA_TOTAL")
plt.show()

#gera o histograma com as notas de matematica
sns.histplot(nzero, x = "NU_NOTA_MT")
plt.show()

#gera o histograma com as notas de linguagem e codigos
sns.histplot(nzero, x = "NU_NOTA_LC")
plt.show()

#gera o histograma com as notas totais e com o acesso a internet ou não dos participantes
sns.histplot(nzero, x = "NU_NOTA_TOTAL", hue = "Q025", kde = True) #a função kde adiciona uma linha de contorno para meu histograma
#o eixo x diz respeito a quantidade de alunos com acesso a internet ou não, onde o gráfico azul expressa a curva para os alunos com internet e o laranja sem acesso a internet
#o eixo Y mostra a nota total desses alunos
plt.show()

#gera o histograma com as notas totais e com o acesso a internet ou não dos participantes
sns.histplot(nzero, x = "NU_NOTA_TOTAL", hue = "Q025", kde = True, stat = "probability")#a função stat gera para o gráfico regras estatisticas, neste caso, a probabilidade do evento ocorrer
plt.show()

sns.histplot(nzero, x = "NU_NOTA_TOTAL", hue = "Q025", kde = True, stat = "probability", cumulative = True)#a função cumulative permite comparar o topo de cada curva
plt.show()

#gera um scatter plot e compara as notas de matematica e de linguagem e codigos
plt.figure(figsize=(10, 10))
sns.scatterplot(data = nzero, x = "NU_NOTA_MT", y = "NU_NOTA_LC")
plt.xlim(-50, 1050)#define o limite inferior e superior para o eixo X
plt.ylim(-50, 1050)#define o limite inferior e superior para o eixo y
#assim, podemos definir um padrão de escala para nosso gráfico
#Esse gráfico mostra se existe alguma relação entre as notas de matematica e de linguagem e codigos
plt.show()

#gera o pairplot para todas as notas de todas as provas, utilizando com parametro as nostas não zero
sns.pairplot(nzero[provas])
plt.show()

#calculo da correlação
correlacao = nzero [provas].corr()
#a maior correlação é entre as notas de linguagem e códigos e ciências da natureza
print(correlacao)

#cria um mapa de calor com a correlação entre as notas
sns.heatmap(correlacao, cmap="Blues", center = 0, annot = True)#cmap define a cor utilizada no gráfico; center define um centro para meu gráfico e annot coloca numericamente a correlação entre cada nota
plt.show()
