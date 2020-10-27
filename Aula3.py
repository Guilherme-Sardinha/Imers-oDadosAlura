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

