"""
2) Elabore um programa que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 50 calcule o excesso de pagamento armazenando-o na variável E, caso contrário zerar tal variável. A hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente.

"""

import os
os.system("cls")

print("""            _            _             _                  _   __       _       
           | |          | |           | |                | | /_/      (_)      
   ___ __ _| | ___ _   _| | ___     __| | ___   ___  __ _| | __ _ _ __ _  ___  
  / __/ _` | |/ __| | | | |/ _ \   / _` |/ _ \ / __|/ _` | |/ _` | '__| |/ _ \ 
 | (_| (_| | | (__| |_| | | (_) | | (_| |  __/ \__ \ (_| | | (_| | |  | | (_) |
  \___\__,_|_|\___|\__,_|_|\___/   \__,_|\___| |___/\__,_|_|\__,_|_|  |_|\___/ 
                                                                               
                                                                               """)

cod_operario = input("Informe o seu código de operário: ")
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))

if horas_trabalhadas > 50:
   
   horas_extras = horas_trabalhadas - 50
   
   salario = horas_trabalhadas * 10
   salario_excendente = horas_extras * 20
   

   salario_total = salario + salario_excendente

   print(f"""O seu salário total é de R$ {salario_total}
Seu salário padrão é de R${salario}
Seu excendente é de R${salario_excendente}
""")
else:
   
   salario_total = (horas_trabalhadas * 10)
   print(f"O seu salário total é de {salario_total}")