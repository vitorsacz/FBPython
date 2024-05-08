"""
1- A prefeitura de uma cidade fez uma pesquisa entre 3 de seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:   

a) média do salário da população; 
b) média do número de filhos; 
c) maior salário; 
d) percentual de pessoas com salário até R$100,00. 

"""

import os
os.system("cls")

NUM_HABITANTES = 3
maior_salario = 0.0
soma_salario = 0.0
maior_que_cem = 0


for pesquisa in range(NUM_HABITANTES):

    salario = float(input("Digite seu salário"))
    filho = int(input("Digite o número de filhos"))
    
    if salario > maior_salario:
        maior_salario = salario

    if salario >= 100:
        maior_que_cem += 1

    soma_salario += salario

    








