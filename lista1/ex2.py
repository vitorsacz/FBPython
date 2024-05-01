"""
    2. Faça um programa que leia a idade de uma pessoa expressa em dias
    e mostre-a expressa em anos, meses e dias 
    (considere ano 365 dias, mês 30 dias)
"""

import os 
os.system("cls") 


idade_em_dias = int(input("Qual o numero de dias? "))

anos = idade_em_dias//365
meses = (idade_em_dias%365)//30
dias = (idade_em_dias%365)%30

print(f"Você possui {anos} anos, {meses} meses e {dias} dias")
