import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

#Traz a uma amostra aleatória dos dados do Enem
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#Pede para o pandas ler o arquivo CSV fruto de parte dos dados do Enem
dados = pd.read_csv(fonte)

provas = ['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_REDACAO']

dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)

zero = dados.query('NU_NOTA_TOTAL==0')
nzero = dados.query('NU_NOTA_TOTAL!=0')

prova_entra = ["NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_CN", "NU_NOTA_REDACAO"]
prova_saida = "NU_NOTA_MT"

notas_entra = nzero[prova_entra]
notas_saida = nzero[prova_saida]

x = notas_entra
y = notas_saida


x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.25)


print(x_treino.head())
