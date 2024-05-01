"""
7) Receber valores de base e altura de um triângulo e verificar se são valores válidos (positivos maiores que zero). Em caso afirmativo, calcular a área do triângulo.

"""


import os
os.system("cls")

base = int(input("Qual a base do triângulo: "))
altura = int(input("Qual a altura do triângulo: "))

if base > 0 and altura > 0:
    area = (base * altura) / 2

print(f"\nA área do triângulo é {area}")