import time
import os
import funcoes as f

class Conta:

    def __init__(self, numero, cpf, saldo, ativo = False):
        self.numero = numero
        self.cpf = cpf
        self.saldo = saldo
        self.ativo = ativo

    def ativar(self):
        
        if self.ativo:
            print("Conta já ativada")
        else:
            self.ativo = True
            print("Conta ativada")


    def credito(self, valor):
        if valor <= 0:
            f.limpa_tela()
            print("Valor inválido")
            time.sleep(1.5)
        else:
            self.saldo += valor


    def debito(self, valor):

        if valor <= 0:
            f.limpa_tela()
            print("Valor inválido")
            time.sleep(2)
            
        elif self.saldo >= valor:
            self.saldo -= valor
        else:
            f.limpa_tela()
            print("Saldo Insuficiente")
            time.sleep(1)
    
    def extrato(self):
        print(f"Saldo atual: R${ self.saldo:.2f}")
        

class Poupanca(Conta):

    def __init__(self, numero, cpf, saldo, diaAniversarioPoupanca, ativo=False, ):
        super().__init__(numero, cpf, saldo, ativo)

        self.diaAniversarioPoupanca = diaAniversarioPoupanca

    def correcao(self, data_aniversario):
        if data_aniversario == self.diaAniversarioPoupanca:

            self.saldo += (self.saldo * 0.05)
            print("\n\nParabéns pelo seu aniversário!")
            print(f"Saldo corrigo para R${ self.saldo:.2f}")


class Corrente(Conta):

    def __init__ (self, numero, cpf, saldo, contator_talao = 0, ativo = False):
        super().__init__(numero, cpf, saldo, ativo)

        self.contator_talao = contator_talao

    def pedi_talao(self, quantidade):
        
        if self.contator_talao == 3:
            print("Todos talões usados!")
        
        elif (quantidade*30) > self.saldo:
            print("Você não possui saldo suficiente para pedir um talão!")
        else: 
            print("Solicitando o talão")
            self.debito(30*quantidade)
            self.contator_talao += quantidade
            self.extrato()
            print(f"talões utilizados {self.contator_talao}")
            time.sleep(3)






        # if (quantidade*self.saldo) < 90 :
        #     if self.contator_talao == 3:
        #         print("Você atingiu o limite de talões!")


        #     else:
        #         self.saldo -= (30*quantidade)
        #         self.contator_talao += quantidade
        #         self.extrato()
        #         print(f"talões usados {self.contator_talao}")
        #         time.sleep(3)

        # else: 
        #     print("Você não possui saldo suficiente para pedir um talão!")
        #     print("Saldo mínimo de R$30,00 para 1 talão")
        #     time.sleep(3)
        


class Especial(Conta):

    def __init__ (self, numero, cpf, saldo, limite = 1000, ativo = False):
        super().__init__(numero, cpf, saldo, ativo)

        self.limite = limite


    def usarLimite(self, valor):

        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente")
            time.sleep(3)

        elif (self.saldo - valor) < 0:
                diff = self.saldo - valor
                self.saldo = 0
                self.limite += diff

                print(self.extrato())
            
        

    def extrato(self):
        print(super().extrato())
        print(f"Limite disponível: R${ self.limite:.2f}")

    # def debito(self, valor):

    #     if self.saldo 



class Empresa(Conta):

    def __init__(self, numero, cpf, saldo, emprestimoEmpresa = 10000, ativo=False):
        super().__init__(numero, cpf, saldo, ativo)

        self.emprestimoEmpresa = emprestimoEmpresa


    def pedir_emprestimo(self, valor):

        if valor > self.emprestimoEmpresa:
            print("Insuficiente!")

        elif self.emprestimoEmpresa > 0:
            if self.emprestimoEmpresa >= valor:
                self.emprestimoEmpresa -= valor
                self.saldo += valor

                self.extrato()
        else:
            print("Empréstimo não disponível")
            print("Limite insuficiente")

    def extrato(self):
        print(super().extrato())
        print(f"Limite disponível: R${ self.emprestimoEmpresa:.2f}")


class Estudantil(Conta):

    def __init__(self, numero, cpf, saldo, limiteEstudantil = 5000, ativo=False):
        super().__init__(numero, cpf, saldo, ativo)

        self.limiteEstudantil = limiteEstudantil


    def usarEstudantil(self, valor):

        if valor > self.limiteEstudantil:
            print("Limite insuficiente")

        elif self.limiteEstudantil > 0:
            if self.limiteEstudantil >= valor:
                self.limiteEstudantil -= valor
                self.saldo += valor

                self.extrato()
        else:
            print("Empréstimo não disponível")
            print("Limite insuficiente")

            print(f"Saldo atual: R${self.saldo:.2f}")
    
    def extrato(self):
        print(super().extrato())
        print(f"Limite estudantil: R${self.limiteEstudantil:.2f}")
        

            

        

        