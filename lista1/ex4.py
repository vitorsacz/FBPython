"""
 Escreva  um sistema que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: 

 D = R + S / 2


 Onde, R = (A + B)²      S = (B + C)²
 """


import os
os.system("cls")
import math


A = int(input("Insira o número A: "))
B = int(input("Insira o número B: "))
C = int(input("Insira o número C: "))

R = pow((A + B), 2)
S = pow((B + C), 2)

D = (R + S) / 2

print(f"o valor de D é {D}")

