"""
    3. Faça umprograma que leia o tempo de duração de um 
    evento em uma fábrica expressa em segundos e 
    mostre-o em horas, minutos e seguntos.
"""

import os 
os.system("cls")

evento = int(input("Informe o tempo do evento em segundos: "))

horas = evento//3600
minutos = (evento%3600)//60
segundos = (evento%3600)%60

print(f"O seu evento de {evento} segundos possui:\n{horas}horas, {minutos} minutos e {segundos} segundos")