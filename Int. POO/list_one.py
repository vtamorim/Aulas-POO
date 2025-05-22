import math
question = int(input("Número da Questão: "))
match question:
    case 1:
        class Circulo:
            def __init__(self,raio):
                self.__raio = raio
            def area(self):
                return math.pi * (self.__raio**2)
            def circuferencia(self):
                return 2 * math.pi * self.__raio
            



        raio = int(input('Raio: '))
        first_cir = Circulo(raio)
        print(f'{first_cir.area():.2f}')
        print(f'{first_cir.circuferencia():.2f}')
    case 2:
        class Viagem:
            def __init__(self,distancia,tempo):
                self.__distancia = distancia
                self.__tempo = tempo
            def vel_media(self):
                return self.__distancia/self.__tempo
            
        distancia = int(input("Distancia: "))
        tempo = int(input("Tempo: "))    
        cal_viagem = Viagem(distancia,tempo)
        print(f'{cal_viagem.vel_media():.0f}')
    case 3:
        class ContaBancaria:
            def __init__(self, nome_titular, numero_conta, saldo):
                self.__nome =  nome_titular
                self.__numero = numero_conta
                self.__saldo = saldo
            def saque(self,saque):
                if saque > self.__saldo:
                    return 'Saldo Insuficiente'
                else:
                    self.__saldo -= saque
                    return self.__saldo
            def deposito(self,deposito):
                if self.__saldo:
                    self.__saldo += deposito
                    return self.__saldo
                else:
                    return 'Erro ao Depositar'
                

        name = input("Nome Titular: ")
        numero = int(input("Número: "))
        saldo = float(input("Por Favor, Digitar seu Saldo: "))
        banquinho = ContaBancaria(name,numero,saldo)
        metodos = ["Saque", "Depósito"]
        for i in range(2):
            print("[",i,"]", metodos[i])
        escolha = int(input("Qual Escolher: "))
        match escolha:
            case 0:   
                saque = float(input("Quanto quer sacar: "))
                print("Escolheu Sacar: ", saque)
                print(banquinho.saque(saque))
            case 1:
                depositar = float(input("Quanto vai querer depositar: "))
                print("Escolheu Depositar: ", depositar)
                print(f'Saldo{banquinho.deposito(depositar)}')
    case 4:
        class Entrada:
            def __init__(self, dia, horario):
                self.__dia = dia
                self.__horario = horario
                self.__valor = 0

            def entrada_int(self):
                self.__valor = 0  
                match self.__dia:
                    case 'Segunda' | 'Terça' | 'Quinta': 
                        self.__valor = 16.00
                    case 'Quarta':
                        self.__valor = 8.00
                    case 'Sexta' | 'Sábado' | 'Domingo':
                        self.__valor = 20.00

               
                if 17 < self.horario < 24:
                    self.__valor += self.__valor * 0.5  

                return self.__valor

            def meia_int(self):
                self.__valor = 0  
                match self.__dia:
                    case 'Segunda' | 'Terça' | 'Quinta':  
                        self.__valor = 8.00
                    case 'Quarta':
                        self.__valor = 8.00
                    case 'Sexta' | 'Sábado' | 'Domingo':
                        self.__valor = 10.00

                
                if 17 < self.__horario < 24:
                    self.__valor += self.__valor * 0.5  

                return self.__valor



        dia = input("Dia da Semana (começando com letra maiúscula): ")
        horario = int(input('Horário (em horas, entre 0 e 23): '))

        EntradinhaInteira = Entrada(dia, horario)
        EntradinhaMeia = Entrada(dia, horario)

        print(f"Entrada Inteira: {EntradinhaInteira.entrada_int()}")  
        print(f"Meia-entrada: {EntradinhaMeia.meia_int()}")          
