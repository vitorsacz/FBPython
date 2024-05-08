"""
6) Elabore um programa que dada a idade de um nadador classifique-o em uma das seguintes categorias:
Infantil A = 5 a 7 anos
Infantil B = 8 a 11 anos
Juvenil A = 12 a 13 anos
Juvenil B = 14 a 17 anos
Adultos = Maiores de 18 anos


"""
import os
import time



while True:
    try:

        os.system("cls")

        idade = int(input("Digite a idade do nadador: "))

        if  5 >= idade <= 7:
            print("Categoria: Infantil A")

        elif 8 >=  idade <= 11:
            print("Categoria: Infantil B")

        elif 12 >= idade <= 13:
            print("Categoria: Juvenil A")

        elif 14 >= idade <= 17:
            print("Categoria: Juvenil B")

        elif  idade >= 18:
            print("Categoria: Adultos")



        time.sleep(1.5)
        print("""\n
O QUE VOCE GOSTARIA DE FAZER?
                    
[1] - Inserir nova idade
[2] - Sair
        """)    

        op = int(input("\nInforme sua opção: "))
        
        if op == 1:
            continue
        elif op == 2:
            print("Obrigado por utilizar nosso sistema!")
            break

    except: 
        print("Não possuímos sua categoria, volte em alguns anos!")


    
        