#Desafio4: Colocar (plotar) os histogramas das idades dos treineiros e não treineiros


import pandas as pd #importa a biblioteca pandas e define um apelido

import matplotlib.pyplot as plt #importa a biblioteca Matplot e define um apelido

#busca a fonte de dados
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#lê o arquivo csv e define este valor para a variavel dados
dados = pd.read_csv(fonte)

#Cria uma variavel que irá receber o valor de duas querys, aprimeira onde selecionamos os treineiros e a segunda onde selecionamos os não treineros
apresenta = (dados.query("IN_TREINEIRO == 1")["NU_IDADE"].sort_index(),dados.query("IN_TREINEIRO == 0")["NU_IDADE"].sort_index())

#cria o boxplot utilizando as duas querys
plt.boxplot(apresenta)

#Adiciona um titulo ao grafico
plt.title('Comparação idade de treineros e não treineros')
#Coloca o nome para o eixo X
plt.xlabel('Treinero  1, Não treinero 2')
#Coloca o nome para o eixo Y
plt.ylabel('Idade')
#mostra o boxplot
plt.show()