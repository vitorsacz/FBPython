"""
3) Desenvolva um programa em que:
Leia 4 (quatro) números;
Calcule o quadrado de cada um;
Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
Caso contrário, imprima os valores lidos e seus respectivos quadrados.


"""

import os
os.system("cls")

import math

num1 = int(input("Informe o numero 1: "))
num2 = int(input("Informe o numero 2: "))
num3 = int(input("Informe o numero 3: "))
num4 = int(input("Informe o numero 4: "))

num1_quadrado = pow(num1, 2)
num2_quadrado = pow(num2, 2)
num3_quadrado = pow(num3, 2)
num4_quadrado = pow(num4, 2)

if num3_quadrado >= 1000:
    print(f"\nO valor do quadrado do número {num3}, é {num3_quadrado}.")
else:
    print(f"""
        Os valores e seus respectivos quadrados:
          
        {num1} => {num1_quadrado}
        {num2} => {num2_quadrado}
        {num3} => {num3_quadrado}
        {num4} => {num4_quadrado}
""")
