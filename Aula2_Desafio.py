#O quão comum é um participante residente de um estado realizar a prova em outro estado?
#Existe alguma caracteristica em comum entre essas pessoas?

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

m = dados.query("SG_UF_RESIDENCIA != SG_UF_PROVA & NU_NOTA_TOTAL == 0")

meio = pd.DataFrame(m, columns =['SG_UF_RESIDENCIA','SG_UF_PROVA','NU_NOTA_TOTAL','Q006'])

zero = dados.query('NU_NOTA_TOTAL==0')

Renda_Organizada = dados["Q006"].unique()

Renda_Organizada.sort()

proporcao = len(m)/len(zero)

print(proporcao * 100)

print(meio)