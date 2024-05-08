import os
import time 
import funcoes

os.system("cls")



def menu():

    while True:
        os.system("cls")
        funcoes.cabecalho()
        opcao = int(input("Informe a sua opção: "))

        if opcao == 1:
            funcoes.cadastrar_produto()

        elif opcao == 2:
            funcoes.listar_produtos()

        elif opcao == 3:
            funcoes.alterar_produto()

        elif opcao == 4:
            
            funcoes.excluir_produto()

        elif opcao == 5:
            funcoes.comprar_produto()      
        
        elif opcao == 6:
            funcoes.saida()
            break

        elif opcao == 7:
            funcoes.preencher_produtos()
            
        
        else:
            print("Opção inválida!")
            time.sleep(2)

        continuar = int(input("\nRealizar outra operação?\n\n1- Sim\n2- Não\n"))

        if continuar == 2:
            funcoes.saida()
            break
        

        

        


if __name__ == "__main__":
    menu()