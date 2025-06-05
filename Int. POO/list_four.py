number_question = int(input("Número da Questão: "))
match number_question:
    case 1:
        class Viagem:
            def __init__(self,dest,dist,lt):
                self.__dest = dest
                self.__dist = dist
                self.__lt = lt
            
            def set_destino(self, newdest):
                if isinstance(newdest,(str)):
                    self.__dest = newdest
                else:
                    raise ValueError("Destino Inválido")
            
            def set_distancia(self, newdist):
                if isinstance(newdist,(float,int)):
                    self.__dist = newdist
                else:
                    raise ValueError("Distância Inválida")        

            def set_litros(self, newlitros):
                if isinstance(newlitros,(float,int)):
                    self.__lt = newlitros
                else:
                    raise ValueError("Número Inválido")         

            def get_destino(self):
                return self.__dest
            
            def get_distancia(self):
                return self.__dist
            
            def get_litros(self):
                return self.__lt

            def Consumo(self):
                return self.__dist / self.__lt

            def __str__(self):
                return f"Destino: {self.__dest}\nDistância: {self.__dist}\nLitros: {self.__lt}"
        class ViagemUI:
            @staticmethod
            def Menu():
                lista_opcoes = ["Calcular","Fim"]
                print("Escolha uma Funcionalidade:")
                for i in range(len(lista_opcoes)):
                    print("[", i ,"]", lista_opcoes[i])
                escolha = input()
                return escolha
            @staticmethod
            def Main():
                running = True
                while running:
                    escolha = ViagemUI.Menu()
                    if escolha == "0":
                        ViagemUI.Calculo()
                    elif escolha == "1":
                        quit("Fim do Código. Tchau")
                    else:
                        ValueError("Valor Inválido, Tente Novamente")                
            @staticmethod
            def Calculo():
                destino  = input("Destino Desejado: ")
                distancia = float(input("Distância ao Destino: "))
                litros = float(input("Litros: "))
                viagem_cliente = Viagem(destino,distancia,litros)
                print(viagem_cliente.__str__())
                print("Cálculo do Consumo Médio: ", viagem_cliente.Consumo())

        if __name__ == "__main__":
            ViagemUI.Main()

    case 2:
        class Pai:
            def __init__(self,n,p,a):
                self.__n = n
                self.__p = p
                self.__a = a
            def set_n(self,newn):
                if isinstance(newn,(str)):
                    self.__n = newn
                else:
                    raise ValueError("Nome Inválido")
            def set_a(self,newa):
                if isinstance(newa,(float)):
                    self.__a = newa
                else:
                    raise ValueError("Área Inválida")
            def set_p(self,newp):
                if isinstance(newp,(int)):
                    self.__p = newp
                else:
                    raise ValueError("Número Inválido")
                
            def get_a(self):
                return self.__a
            def get_n(self):
                return self.__n
            def get_p(self):
                return self.__p
            
            def Densidade(self):
                return self.__p/self.__a
            
            def __str__(self):
                return f"Nome: {self.__n}\nPopulação: {self.__p} Pessoa(s)\nÁrea: {self.__a}"
            

        class ParcialUI:
            @staticmethod
            def Menu():
                lista_opcoes = ["Calcular","Fim"]
                print("Escolha uma Funcionalidade:")
                for i in range(len(lista_opcoes)):
                    print("[", i ,"]", lista_opcoes[i])
                escolha = input()
                return escolha
            @staticmethod
            def Main():
                running = True
                while running:
                    escolha = ParcialUI.Menu()
                    if escolha == "0":
                        ParcialUI.Calculo()
                    elif escolha == "1":
                        quit("Fim do Código. Tchau")
                    else:
                        ValueError("Valor Inválido, Tente Novamente")                
            @staticmethod
            def Calculo():
                name_country  = input("Nome do País: ")
                populacao = int(input("População do País: "))
                area = float(input("Area da População: "))
                pai_densidade = Pai(name_country,populacao,area)
                print(pai_densidade.__str__())
                print("Cálculo da Densidade: ", pai_densidade.Densidade())

        if __name__ == "__main__":
            ParcialUI.Main()