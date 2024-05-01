"""
Um sistema de equações lineares do tipo: 

ax + bx = c
dx + ey = f

pode ser resolvido segundo mostrado abaixo : 

x = ce - bf / ae - bd

y = af - cd / ae - bd

Escreva um programa que lê os coeficientes a,b,c,d,e e f e calcula e mostra os valores de x e y. 
"""

import os
os.system("cls")

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))  
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))


x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print(f"\nO valor de X é : {x} \nO valor de Y é: {y}")



