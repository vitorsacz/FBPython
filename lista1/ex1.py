"""
1. Faça um programa que leia a idade de uma pessoa expressa em anos, 
meses e dias e mostre-a expressa apenas em dias 
(considere o ano 365 dias, m^ês 30 dias)

"""

import os 
os.system("cls")

nome = input("Qual o seu nome? ")
ano_atual = 2024

idade = int(input("Qual anos voce tem? "))
mes_nasc = int(input("Qual mês voce nasceu? "))
dia_nasc = int(input("Qual dia voce nasceu? "))

ano_em_dias = idade * 365
mes_em_dias = mes_nasc * 30

idade_em_dias = dia_nasc + mes_em_dias + ano_em_dias

print(f"Olá { nome }, voce tem cerca de { idade_em_dias } dias de vida!")

