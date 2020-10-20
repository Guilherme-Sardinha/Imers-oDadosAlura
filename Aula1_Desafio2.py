#Descobrir de quais estados são os inscritos com 13 anos.
import pandas as pd #importa a biblioteca pandas e define um apelido

import matplotlib.pyplot as plt #importa a biblioteca Matplot e define um apelido

#busca a fonte de dados
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#lê o arquivo csv e define este valor para a variavel dados
dados = pd.read_csv(fonte)

#Cria uma query para cruzar a informação da coluna de idade com a coluna de estado
coluna = dados.query("NU_IDADE == 13")["SG_UF_RESIDENCIA"]

#mostra em tela a tabela
print(coluna)
