#Desafio5: comparar as distribuições das provas em inglês e espanhol (Criar histograma e boxplot)

import pandas as pd

import matplotlib.pyplot as plt

#Traz a uma amostra aleatória dos dados do Enem
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#Pede para o pandas ler o arquivo CSV fruto de parte dos dados do Enem
dados = pd.read_csv(fonte)

#Cria uma variavel prova para armazenar os valores para as querys de Espanhol e ingles
prova = len(dados.query("TP_LINGUA == 1")["TP_LINGUA"]), len(dados.query("TP_LINGUA == 0")["TP_LINGUA"])

#cria um histograma
plt.hist(prova)
plt.show()