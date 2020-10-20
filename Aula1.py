#Faz o impor da biblioteca pandas
import pandas as pd

import matplotlib.pyplot as plt

#Traz a uma amostra aleatória dos dados do Enem
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#Pede para o pandas ler o arquivo CSV fruto de parte dos dados do Enem
dados = pd.read_csv(fonte)

#Exibe a tabela
print(dados.head())

#Exibe os valores da coluna 'SG_UF_RESIDENCIA'
print(dados["SG_UF_RESIDENCIA"])

#Exibe todas as colunas presentes na tabela
print(dados.columns.values)

#Exibe os valores das colunas 'SG_UF_RESIDENCIA' e 'Q025'
print(dados[["SG_UF_RESIDENCIA","Q025"]])

#Exibe os membros da coluna 'SG_UF_RESIDENCIA'
print(dados["SG_UF_RESIDENCIA"].unique())

#Exibe a quantidade membros da coluna 'SG_UF_RESIDENCIA'
print(len(dados["SG_UF_RESIDENCIA"].unique()))

#Exibe a frequencia de cada membro da coluna 'SG_UF_RESIDENCIA'
print(dados["SG_UF_RESIDENCIA"].value_counts())

#Exibe a frequencia de cada membro da coluna 'NU_IDADE'
print(dados["NU_IDADE"].value_counts())

#Organiza de maneira crescente as idades e exibe a frequencia que essa idade se repete
print(dados["NU_IDADE"].value_counts().sort_index())

#Gera um histograma a partir da coluna 'NU_IDADE'
dados["NU_IDADE"].hist()
#Adiciona um titulo ao meu histograma
plt.title("Idade dos participantes")
#Exibe o histograma
plt.show()

#Gera o histograma, altera sua escala e o tamanho da tela
dados["NU_IDADE"].hist(bins = 40, figsize = (10,8) )
plt.show()

#Os participantes do Enem como treinero possuem na tabela o valor 1 associado, esse comando conta a quantidade de treineros por idade
print(dados.query("IN_TREINEIRO == 1")["NU_IDADE"].value_counts().sort_index())

#Gera um histograma a partir das notas da redação
dados ["NU_NOTA_REDACAO"].hist(bins = 20, figsize=(8, 6))
plt.show()

#Gera um histograma a partir das notas de liguagens e códigos
dados ["NU_NOTA_LC"].hist(bins = 20, figsize=(8, 6))
plt.show()

#Mostra a média das notas de redação
print(dados["NU_NOTA_REDACAO"].mean())

#Mostra o desvio padrão das notas de redação
print(dados["NU_NOTA_REDACAO"].std())

#Passa para a variavel 'prova' os valores das colunas
provas = ["NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_MT","NU_NOTA_LC","NU_NOTA_REDACAO"]
#Apresenta a quantidade, a média, o desvio padrão, o valor minimo, o primeiro quartil, a mediana, o terceiro quartil e o maximo
print(dados[provas].describe())

#Apresenta o quantil mais a direita (90%)
print(dados["NU_NOTA_LC"].quantile(0.9))

#Gera um box plot com as linhas de referencia ao fundo
dados["NU_NOTA_LC"].plot.box(grid = True, figsize = (8, 6))
plt.show()

#Gera um box plot com a nota de todas as provas
dados[provas].plot.box(grid = True, figsize= (10, 8))
plt.show()

