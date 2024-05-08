import os
import time 

produtos = []
carrinho = []

def cadastrar_produto():
    os.system('cls')
    while True:
                
        nome = input("informe o nome do produto: ")
        valor = float(input("informe o valor do produto: "))
        descricao = input("informe a descricao do produto: ")
    

        produtos.append({
            "nome": nome,
            "valor": valor,
            "descricao": descricao,
            "estoque": 10
        })

        print("Produto adicionado com sucesso")

        continuar = int(input("\nDeseja continuar cadastrando produtos?\n1- Sim\n2- Não\n"))

        if continuar == 2:
            break
        print("\n")


def listar_produtos():
    os.system('cls')

    if len(produtos) == 0:
        print("Não existem produtos cadastrados")
        print("Cadastre produtos")
        return False
        time.sleep(1.5)

        
    
    else:
        for indice, item in enumerate(produtos):
            print("\n")
            print(f"codigo: {indice}")
            time.sleep(0.5)

            for chave in item:
                print(f"{chave}: {item[chave]}\t")

        print("\n")


def listar_carrinho():
    os.system('cls')

    if len(carrinho) == 0:
        print("Não existem produtos adicionados ao carrinho")
        print("Adicione produtos")
        return False
        time.sleep(1.5)

        
    
    else:
        for indice, item in enumerate(carrinho):
            print("\n")
            print(f"codigo: {indice}")
            time.sleep(0.5)

            for chave in item:
                print(f"{chave}: {item[chave]}\t")

        print("\n")




def excluir_produto():

    codigo = int(input("\nInforme o código do produto gostaria excluir: "))

    if 0<= codigo < len(produtos):
        
        certeza_decisao = int(input("\nCerteza que deseja excluir o produto?\n\n1- Sim\n2- Não\n"))

        if certeza_decisao == 1:
            produtos.remove(produtos[codigo])
            print("\nProduto excluido com sucesso")    
    else:
        print("\nProduto não encontrado")

    print("\n")



def comprar_produto():
    listar_produtos()

    if listar_produtos() == False:
        return
    
    else:
        codigo = int(input("Informe o código do produto: ") )
        quantidade = int(input("Informe a quantidade desejada: "))

        if 0<= codigo < len(produtos):

            if produtos[codigo]["estoque"] > 0:
                if produtos[codigo]["estoque"] >= quantidade:
                    produtos[codigo]["estoque"] -= quantidade

                    carrinho.append({"nome": produtos["nome"], "valor": produtos["valor"], "descricao": produtos["descricao"], "estoque": quantidade })

                    print("Produto adicionado ao carrinho com sucesso")
                    listar_carrinho()
            else:
                ("Quantidade solicitada indisponivel no estoque!")

            
        else:
            print("Produto não encontrado")

    print("\n")






def alterar_produto():

    listar_produtos()

    codigo = int(input("informe o código do produto que voce deseja inserir no carrinho: "))

    if 0 <= codigo < len(produtos):

        print("O que deseja alterar?\n\n")
        print("1- Nome \n2- Valor\n 3- Descrição")
        opcao = int(input("Informe a opção desejada: "))

        if opcao == 1:
            nome = input("Informe o novo nome: ")
            produtos[codigo]["nome"] = nome

        elif opcao == 2:
            valor = float(input("Informe o novo valor: "))
            produtos[codigo]["valor"] = valor

        elif opcao == 3:
            descricao = input("Informe a nova descrição: ")
            produtos[codigo]['descricao'] = descricao

    print("\n")


def cabecalho():
    print("""                             
                             
  _ __ ___   ___ _ __  _   _ 
 | '_ ` _ \ / _ \ '_ \| | | |
 | | | | | |  __/ | | | |_| |
 |_| |_| |_|\___|_| |_|\__,_|
          
1- CADASTRAR PRODUTOS
2- LISTAR PRODUTOS
3- ALTERAR PRODUTOS
4- EXCLUIR PRODUTOS
5- REALIZAR COMPRAS
6- SAIR
""")
    
def saida():
    print("""                        
       | |        (_)               | |                         
   ___ | |__  _ __ _  __ _  __ _  __| | ___    _ __   ___  _ __ 
  / _ \| '_ \| '__| |/ _` |/ _` |/ _` |/ _ \  | '_ \ / _ \| '__|
 | (_) | |_) | |  | | (_| | (_| | (_| | (_) | | |_) | (_) | |   
  \___/|_.__/|_|  |_|\__, |\__,_|\__,_|\___/  | .__/ \___/|_|   
                      __/ |                   | |               
                     |___/                    |_|""")
    print("""
   ___ ___  _ __ ___  _ __  _ __ __ _ _ __    ___ ___  _ __   ___  ___  ___ ___  
  / __/ _ \| '_ ` _ \| '_ \| '__/ _` | '__|  / __/ _ \| '_ \ / _ \/ __|/ __/ _ \ 
 | (_| (_) | | | | | | |_) | | | (_| | |    | (_| (_) | | | | (_) \__ \ (_| (_) |
  \___\___/|_| |_| |_| .__/|_|  \__,_|_|     \___\___/|_| |_|\___/|___/\___\___/ 
                     | |                                                         
                     |_|""")

   
#USADA APENAS PARA TESTES NA PRINCIPAL, SEM PRECISAR CADASTRAR PRODUTOS ANTES
def preencher_produtos():
    # Exemplo de preenchimento da lista de produtos
    produtos.append({"nome": "Produto A", "valor": 10.0, "descricao": "Descrição do Produto A", "estoque": 10})
    produtos.append({"nome": "Produto B", "valor": 20.0, "descricao": "Descrição do Produto B",  "estoque": 10})
    produtos.append({"nome": "Produto C", "valor": 30.0, "descricao": "Descrição do Produto C",  "estoque": 10})  



        


    
