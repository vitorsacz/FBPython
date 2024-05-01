"""
8) Construa um programa para ler uma variável numérica N e imprimi-la somente se a mesma for maior que 100, caso contrário imprimi-la com o valor zero.

"""


import os
os.system("cls")

numero = float(input("Informe um número qualquer: "))

if numero > 100:
    print(numero)
else:
    numero = 0
    print(numero)