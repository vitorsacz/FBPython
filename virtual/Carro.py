class CarroPequeno:

    def __init__(self, marca, cor, motor, velocidade = 0, ligado = False) -> None:

        self.cor = marca
        self.marca = cor
        self.motor = motor
        self.velocidade = velocidade
        self.ligado = ligado 

    def ligar_carro(self):

        if self.ligado == False:
            self.ligado = True
            print("Carro Ligado -> VRUMMMMM")
        else:
            print("O carro já está ligado")
            

    def desligar_carro(self):

        if self.ligado == True:
            self.ligado = False
            print("Carro desligado")
        else:
            print("O carro já está desligado")


    def acelerar_carro(self):

        if self.ligado == True:
            if self.velocidade <= 190:
                print(f"Velocidade atual: {self.velocidade}Km/h")
                print("Acelerando...")
                self.velocidade += 10
                print(f"Velocidade atual: {self.velocidade}Km/h")
            else:
                print("O carro está no seu limite.")

        else:
            print("O carro está desligado. Ligue o carro!")



    def frear_carro(self):

        if self.ligado:
            if self.velocidade >= 10:
                print(f"Velocidade atual: {self.velocidade}Km/h")
                print("Desacelerando...")

                self.velocidade -= 10

                print(f"Velocidade atual: {self.velocidade}Km/h")
            else:
                print("O carro está parado.")
        else:
            print("O carro está desligado. Ligue o carro!")
        

        



class Moto:

    def __init__(self, marca, cilindradas, velocidade = 0, ligado = False) -> None:
        #exemplo de atributos privados
        self.__marca = marca
        self.__cilindradas = cilindradas
        self.__velocidade = velocidade
        self.__ligado = ligado 


class CarroGrande:

    def __init__(self, marca, cor, motor, eixos, velocidade = 0, ligado = False) -> None:

        self.cor = marca
        self.marca = cor
        self.motor = motor
        self.eixos = motor
        self.velocidade = velocidade
        self.ligado = ligado 



    