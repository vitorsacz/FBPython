from Contas import Poupanca, Corrente, Especial, Empresa, Estudantil
import funcoes as f

import os
import time

def main():
    
    pop = Poupanca(45232, 47903098377, 0.0, 21)
    cor = Corrente(23465, 47903098377, 0.0)
    esp = Especial(83746, 47903098377, 0.0)
    em = Empresa(12938, 47903098377, 0.0)
    estu = Estudantil(91474, 47903098377, 0.0)

    num_mov = 3

    while True:
        f.cabecalho()

        opcao = f.menu()
        movimento = 0

        if opcao == 1:
            tipo_conta = 'POUPANÇA'

            for i in range(num_mov):
            
                f.cabecalho_conta(tipo_conta, i+1)

                pop.extrato()

                opcao = f.opcao_movimento()
                if opcao == 1:
                    valor = float(input("Qual o valor do depósito? "))
                    
                    time.sleep(1)
                    pop.credito(valor)

                elif opcao == 2:
                    valor = float(input("Qual o valor do saque? "))

                    time.sleep(1)
                    pop.debito(valor)
                    

            dia = int(input("Qual o dia de hoje? "))
            pop.correcao(dia)

            if i+1 == num_mov:
                    f.cabecalho_conta(tipo_conta, i+1)
                    em.extrato()
                    time.sleep(3)

        elif opcao == 2:
            tipo_conta = 'CORRENTE'

            for i in range(num_mov):
                
                f.cabecalho_conta(tipo_conta, i+1)

                cor.extrato()

                opcao = f.opcao_movimento()
                if opcao == 1:
                    valor = float(input("Qual o valor do depósito? "))

                    cor.credito(valor)
                    time.sleep(1)

                    f.cabecalho_conta(tipo_conta, i+1)
                    cor.extrato()
                    time.sleep(1)
                    

                elif opcao == 2:
                    valor = float(input("Qual o valor do saque?"))
                    cor.debito(valor)
                    
                    f.cabecalho_conta(tipo_conta, i+1)
                    cor.extrato()
                    time.sleep(1)
                    

            pedido_talao = input("Gostaria de pegar um talão de cheque? S/N\n").upper()

            if pedido_talao == 'S':
                quantidade_taloes = int(input("Quantos talões você gostaria?"))
                cor.pedi_talao(quantidade_taloes)
                time.sleep(3)

            elif i+1 == num_mov:
                    f.cabecalho_conta(tipo_conta, i+1)
                    esp.extrato()
                    time.sleep(3)
                
            
        elif opcao == 3:
            tipo_conta = 'ESPECIAL'

            for i in range(num_mov):
            
                f.cabecalho_conta(tipo_conta, i+1)

                esp.extrato()

                opcao = f.opcao_movimento()

                if opcao == 1:
                    valor = float(input("Qual o valor do depósito? "))
                    
                    time.sleep(1)
                    esp.credito(valor)

                elif opcao == 2:
                    valor = float(input("Qual o valor do saque? "))
                    
                    if esp.saldo <= valor:
                        time.sleep(1)
                        esp.usarLimite(valor)
                    else:
                        time.sleep(1)
                        esp.debito(valor)

            if i+1 == num_mov:
                    f.cabecalho_conta(tipo_conta, i+1)
                    esp.extrato()
                    time.sleep(3)     

            


        elif opcao == 4:
            tipo_conta = 'EMPRESA'

            for i in range(num_mov):

                f.cabecalho_conta(tipo_conta, i+1)

                em.extrato()

                opcao = f.opcao_movimento()

                if opcao == 1:   
                    valor = float(input("Qual o valor do depósito? "))                    
                    em.credito(valor)
                    time.sleep(1)

                elif opcao == 2: 
                    valor = float(input("Qual o valor do saque? "))

                    if valor > em.saldo:
                        print("\n\nSaldo insuficiente, gostaria de fazer um emprestimo?")
                        print("\nValores disponíveis: ")
                        print(em.extrato())
                        print("\n1- Sim\n2- Não")  

                        escolha_emprestimo = int(input("\nInforme sua escolha:"))

                        if escolha_emprestimo == 1:
                            valor_emprestimo = float(input("Qual o valor do emprestimo? "))

                            em.pedir_emprestimo(valor_emprestimo)

                        elif escolha_emprestimo == 2:
                            print("Continuando...")

                        else:
                            print("Opção inválida")
                    
                    elif em.saldo >= valor:
                        em.debito(valor)

                else:
                    print("Opção inválida")

                if i+1 == num_mov:
                    f.cabecalho_conta(tipo_conta, i+1)
                    em.extrato()
                    time.sleep(3)



            

        elif opcao == 5:
            tipo_conta = 'ESTUDANTIL'

            for i in range(num_mov):

                f.cabecalho_conta(tipo_conta, i+1)

                estu.extrato()

                opcao = f.opcao_movimento()

                if opcao == 1:   
                    valor = float(input("Qual o valor do depósito? "))                    
                    estu.credito(valor)
                    time.sleep(1)

                elif opcao == 2: 
                    valor = float(input("Qual o valor do saque? "))

                    if valor > estu.saldo:
                        print("\n\nSaldo insuficiente, gostaria de fazer um emprestimo?")
                        print("\nValores disponíveis: ")
                        print(estu.extrato())
                        print("\n1- Sim\n2- Não")  

                        escolha_emprestimo = int(input("\nInforme sua escolha:"))

                        if escolha_emprestimo == 1:
                            valor_emprestimo = float(input("Qual o valor do emprestimo? "))

                            estu.usarEstudantil(valor_emprestimo)

                        elif escolha_emprestimo == 2:
                            print("Continuando...")

                        else:
                            print("Opção inválida")
                    
                    elif em.saldo >= valor:
                        estu.debito(valor)

                else:
                    print("Opção inválida")

                if i+1 == num_mov:
                    f.cabecalho_conta(tipo_conta, i+1)
                    estu.extrato()
                    time.sleep(3)


        elif opcao == 6:
            f.saida()
            break
        
        else:
            print("Opção inválida")

        f.limpa_tela()
        f.cabecalho()
        continuar = input("\n\nDeseja continuar? S/N\n").upper

        if continuar == 'N':
            break
    




if __name__ == "__main__":
    main()
