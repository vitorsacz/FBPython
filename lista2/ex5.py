"""
    5) A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um programa que leia o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas.
"""
import os
os.system("cls")

indice_poluicao = int(input("Qual o índice de poluição da sua empresa? "))

if 0.05 <= indice_poluicao <= 0.25:
    print("\nO índice de poluição está aceitável.")

elif 0.26 <= indice_poluicao <= 0.4:
    print("\nO índice de poluição está alto. As indústrias do 1º grupo devem suspender suas atividades.")

elif 0.4 < indice_poluicao <= 0.5:
    print("\nO índice de poluição está muito alto. As indústrias do 1º e 2º grupo devem suspender suas atividades.")