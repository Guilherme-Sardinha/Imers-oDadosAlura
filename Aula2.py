#Correção desafios aula 1
import pandas as pd

import matplotlib.pyplot as plt

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

