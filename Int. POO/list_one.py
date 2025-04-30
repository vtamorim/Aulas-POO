import math
question = int(input("Número da Questão: "))
match question:
    case 1:
        class Circulo:
            def __init__(self):
                self.raio = 0
            def area(self):
                return math.pi * (self.raio*2)
            def circuferencia(self):
                return 2 * math.pi * self.raio
            



        first_cir = Circulo()
        first_cir.raio = int(input('Raio: '))
        print(f'{first_cir.area():.2f}')
        print(f'{first_cir.circuferencia():.2f}')
    case 2:
        class Viagem:
            def __init__(self):
                self.distancia = 0
                self.tempo = 0
            def vel_media(self):
                return self.distancia/self.tempo
            
    
        cal_viagem = Viagem()
        cal_viagem.distancia = int(input("Distancia: "))
        cal_viagem.tempo = int(input("Tempo: "))
        print(f'{cal_viagem.vel_media:.0f}')
    case 3:
        class ContaBancaria:
            def __init__(self, nome_titular, numero_conta, saldo):
                self.nome =  nome_titular
                self.numero = numero_conta
                self.saldo = saldo
            def saque(self,saque):
                if saque > self.saldo:
                    return 'Saldo Insuficiente'
                else:
                    self.saldo -= saque
                    return self.saldo
            def deposito(self,deposito):
                if self.saldo:
                    self.saldo += deposito
                    return self.saldo
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
                self.dia = dia
                self.horario = horario
                self.valor = 0

            def entrada_int(self):
                self.valor = 0  
                match self.dia:
                    case 'Segunda' | 'Terça' | 'Quinta': 
                        self.valor = 16.00
                    case 'Quarta':
                        self.valor = 8.00
                    case 'Sexta' | 'Sábado' | 'Domingo':
                        self.valor = 20.00

               
                if 17 < self.horario < 24:
                    self.valor += self.valor * 0.5  

                return self.valor

            def meia_int(self):
                self.valor = 0  
                match self.dia:
                    case 'Segunda' | 'Terça' | 'Quinta':  
                        self.valor = 8.00
                    case 'Quarta':
                        self.valor = 8.00
                    case 'Sexta' | 'Sábado' | 'Domingo':
                        self.valor = 10.00

                
                if 17 < self.horario < 24:
                    self.valor += self.valor * 0.5  

                return self.valor



        dia = input("Dia da Semana (começando com letra maiúscula): ")
        horario = int(input('Horário (em horas, entre 0 e 23): '))

        EntradinhaInteira = Entrada(dia, horario)
        EntradinhaMeia = Entrada(dia, horario)

        print(f"Entrada Inteira: {EntradinhaInteira.entrada_int()}")  
        print(f"Meia-entrada: {EntradinhaMeia.meia_int()}")          
