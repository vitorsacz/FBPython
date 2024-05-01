#PROGRAMA DA IDADE

import os
os.system("cls")

nome = input("Informe seu nome: ").capitalize()
print(f"Oi, {nome}. Tudo bem?")

ano_atual = 2024
ano_nasc = int(input(" \nDigite o ano do seu nascimento: "))

idade = ano_atual - ano_nasc

print(f"\nOi, {nome}. Sua idade aproximada é {idade}")
