#Correção desafios aula 1
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

#Traz a uma amostra aleatória dos dados do Enem
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#Pede para o pandas ler o arquivo CSV fruto de parte dos dados do Enem
dados = pd.read_csv(fonte)

#########Correção desafio2################
print(dados.query("NU_IDADE == 13"))

#Traz os participantes com 14 anos ou menos, sua residência e apresenta os valores em ordem decrescente por estado
print(dados.query("NU_IDADE <= 14")["SG_UF_RESIDENCIA"].value_counts())

###########Correção desafio1##############
#O 'value_counts(normalize=True)' faz automaticamente a proporção dos inscritos por idade ordenado de forma decrescente de acordo com a frequencia
print(dados["NU_IDADE"].value_counts(normalize=True))

#Cria uma variavel que adquiri o valor da query
alunos_menor_quatorze = dados.query("NU_IDADE <= 14")
#Utiliza soemente a coluna de residencia, ordena os valores em ordem decrescente e cria um grafico em pizza
alunos_menor_quatorze["SG_UF_RESIDENCIA"].value_counts().plot.pie()
plt.show()

#Utiliza somente a coluna de residencia, ordena os valores em ordem decrescente e cria um grafico em barras
alunos_menor_quatorze["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.bar()
plt.show()

#Mostra o tamanho da amostra de alunos com idade menor ou igual a 14 anos
print(len(alunos_menor_quatorze))

#Cria um boxplot utilizando o seaborn com as resposta do questionario 'Q006' que apresenta a renda mensal da familia, onde quanto mais distante de A maior a renda familiar, e cruza essa informação com a nota de matematica
sns.boxplot(x="Q006",y="NU_NOTA_MT", data = dados)
plt.show()


#Cria uma variavel para ordernar os valores, apresentando os valores unicos daquela coluna
Renda_Organizada = dados["Q006"].unique()
#Ordena alfabeticamente a renda
Renda_Organizada.sort()
#Cria o boxplot e ordena seus valores a partir da variavel renda organizada
sns.boxplot(x="Q006",y="NU_NOTA_MT", data = dados, order= Renda_Organizada)
plt.show()

#cria a variavel 'provas'
provas = ['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_REDACAO']
#Realiza a soma de todas as notas da coluna
print(dados[provas].sum())

#Faz a soma baseada na nota de cada um dos inscritos
dados[provas].sum(axis=1) #Axis define a linha que a soma começará a ser feita
#Cria uma nova coluna e utiliza a soma de todas as notas do aluno como valor
dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
#Mostra os 4 primeiros valores da minha tabela
print(dados.head())
#Utiliza a nova coluna criada, 'soma de todas as notas', no eixo y para criar o boxplot
sns.boxplot(x="Q006",y="NU_NOTA_TOTAL", data = dados, order= Renda_Organizada)
plt.show()

#Cria um histograma com as notas totais
sns.displot(dados, x = "NU_NOTA_TOTAL")
plt.show()

#'append' é um comando do Python para adicionar volores completos, seja um objeto ou uma lista
provas.append("NU_NOTA_TOTAL")
#Mostra os alunos que tiraram nota zero em todas as matérias
print(dados[provas].query("NU_NOTA_TOTAL == 0"))

#Criamos uma variavel para verificar se a pessoa tirou zero
dados_sem_zero = dados.query("NU_NOTA_TOTAL != 0")
print(dados_sem_zero.head())
#Geramos um boxplot sem as notas zeradas
sns.boxplot(x="Q006",y="NU_NOTA_TOTAL", data = dados_sem_zero, order= Renda_Organizada)
plt.show()

#Adicionamos com o comando 'hue' um boxplot que compara os alunos treineiros e não treineros
sns.boxplot(x="Q006",y="NU_NOTA_TOTAL", data = dados_sem_zero, order= Renda_Organizada, hue ="IN_TREINEIRO")
plt.show()