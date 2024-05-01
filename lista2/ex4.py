"""
4) Faça um programa que leia um número inteiro e mostre uma mensagem 
indicando se este número é par ou ímpar, e se é positivo ou negativo.

"""

import os
os.system("cls")

numero = int(input("Informe um numero qualquer: "))

if numero > 0:
    if numero % 2 == 0:
        print("O numero é par e positivo")
    else:
        print("O numero é impar e positivo")

elif numero < 0:
    if numero % 2 == 0:
        print("O numero é par e negativo")
    else:
        print("O numero é impar e negativo")

else:
    print("Insira um número válido")

    