"""

1) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de tomate maior que o estabelecido pelo regulamento do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável P (peso de tomates) e verifique se há excesso. Se houver, gravar na variável E (Excesso) e na variável M o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

"""

import os
os.system("cls")

print("""           _            _           _                       _        _                        _            
           | |          | |         | |                     | |      | |                      | |           
   ___ __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _    __| | ___  | |_ ___  _ __ ___   __ _| |_ ___  ___ 
  / __/ _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |  / _` |/ _ \ | __/ _ \| '_ ` _ \ / _` | __/ _ \/ __|
 | (_| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| | | (_| |  __/ | || (_) | | | | | | (_| | ||  __/\__ 
  \___\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|  \__,_|\___|  \__\___/|_| |_| |_|\__,_|\__\___||___/
                                                                                                            
                                                                                                            """)


qtd_tomates = float(input("Informe o valor em Kg dos kilos: "))
multa = 4.00

if qtd_tomates > 50:
    excesso = qtd_tomates - 50
    multa_total = excesso * multa
else:
    excesso = 0
    multa_total = 0

print("\n")
print(f"""Para {qtd_tomates}kg de tomates: 
     
Excesso: {excesso}
Multa: R${multa_total}""")
