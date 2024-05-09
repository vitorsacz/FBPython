import os
import Contas


def cabecalho():

    limpa_tela()

    print(""" 
  ____                           _____                
 |  _ \                         / ____|               
 | |_) | __ _ _ __   ___ ___   | (___   __ _  ___ ____
 |  _ < / _` | '_ \ / __/ _ \   \___ \ / _` |/ __|_  /
 | |_) | (_| | | | | (_| (_) |  ____) | (_| | (__ / / 
 |____/ \__,_|_| |_|\___\___/  |_____/ \__,_|\___/___|""")
    
    print(""" 
  __  ___ __ __ ___ ___ ___   _  _  _  ______  __  __  _ __   __    
/' _/| __|  V  | _,\ _ \ __| | || || |/ _/ _ \/  \|  \| | _\ /__\   
`._`.| _|| \_/ | v_/ v / _|  | || \/ | \_| v / /\ | | ' | v | \/ |  
|___/|___|_| |_|_| |_|_\___| |___\__/ \__/_|_\_||_|_|\__|__/ \__/ """)

    
    

def saida():
    print("""   
   ___  _        _              _                 _     
  / _ \| |__ _ _(_)__ _ __ _ __| |___   _ __  ___| |___ 
 | (_) | '_ \ '_| / _` / _` / _` / _ \ | '_ \/ -_) / _ \.
  \___/|_.__/_| |_\__, \__,_\__,_\___/ | .__/\___|_\___/
                  |___/                |_|              
          """)
        
    print("""
               _                                         
  __ _ __ _ __| |_ __ _ _ _   __ ___ _ _  ___ ___ __ ___ 
 / _` / _` (_-<  _/ _` | '_| / _/ _ \ ' \/ _ (_-</ _/ _ \.
 \__, \__,_/__/\__\__,_|_|   \__\___/_||_\___/__/\__\___/
 |___/                                                  
           """)
    


def menu():

    print("""
1- CONTA POUPANÇA
2- CONTA CORRENTE
3- CONTA ESPECIAL
4- CONTA EMPRESA
5- CONTA ESTUDANTIL
6- SAIR
          
""")
    
    opcao = int(input("Informe a opcão desejada: "))

    return opcao

def cabecalho_conta(tipo_conta, movimentos):

    cabecalho()

    print(f"\nCONTA {tipo_conta}")
    print(f"MOVIMENTO {movimentos}")

    # if tipo_conta == 'ESPECIAL':
    #     print(Contas.Especial.extrato())
    
    # elif tipo_conta == 'EMPRESA':
    #     print(Contas.Empresa.extrato())

    # elif tipo_conta == 'ESTUDANTIL':
    #     print(Contas.Estudantil.extrato())




def opcao_movimento():

    print("\nO QUE DESEJA REALIZAR?")
    print("""
1- CRÉDITO
2- DÉBITO
""")
    opcao_movimento = int(input("Informe a opcão desejada: "))

    return opcao_movimento

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

    






    


    


