"""

Construa um programa que, tendo como dados de entrada dois pontos quaisquer no plano, 
P(x1, y1) e P(x2, y2), escreva a distância entre eles. 
A fórmula que efetua tal cálculo é

D =  √(x²-x1)² + (y2 - y1)²

"""
import os
os.system("cls")

import math

x1 = int(input("Informe o X do ponto 1: "))
y1 = int(input("Informe o Y do ponto 1: "))

ponto1 = (x1, y1)

x2 = int(input("Informe o X do ponto 2: "))
y2 = int(input("Informe o Y do ponto 2: "))

ponto2 = (x2, y2)

D = pow((x2-x1), 2) + pow((y2 - y1), 2)
distancia = math.sqrt(D)

print(f"A distancia entre os pontos é {distancia:.2f}")
