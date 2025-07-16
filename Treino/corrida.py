from datetime import datetime,timedelta

class ControleCorrida:
    def __init__(self,id,name,data,dist,duracao):
        self.__id = id
        self.__name = name
        self.__dist = dist
        self.__duracao = duracao
        self.__data = data
    
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_distancia(self):
        return self.__dist
    def get_data(self):
        return self.__data
    def get_duracao(self):
        return self.__duracao
    
    def set_id(self,newid):
        if newid <= 0: raise ValueError("Identificador Inválido")
        self.__id = newid
    def set_name(self,newname):
        if newname == "": raise ValueError("Nome inválido")
        self.__name = newname
    def set_distancia(self,newdist):
        if newdist <= 0: raise ValueError("Distância Inválida")
        self.__dist = newdist
    def set_data(self,newdata):
        if not isinstance(newdata,(datetime)): raise ValueError("Data inválida")
        self.__data = newdata
    def set_duracao(self,newduracao):
        if not isinstance(newduracao,(timedelta)): raise ValueError("Duração Inválida")
        self.__duracao = newduracao
    
    def velocidade_media(self):
        return self.__dist/self.__duracao.total_seconds()
    def __str__(self):
        return f"Identificador: {self.__id} Nome: {self.__name} Data: {self.__data} Distância: {self.__dist} Duração: {self.__duracao} "

class ControleCorridaUI:
    __listacorrida = []
    __contador = 0
    @classmethod
    def menu(cls):
        opcoes = ["Inserir Nova Corrida","Listar todas as Corridas","Mostrar Corrida Mais Longa","Atualizar Corrida","Excluir Corrida","Corrida Mais Rápida","Fim"]
        for i in range(len(opcoes)):
            print("[", i,"]", opcoes[i])
        return int(input())
    @classmethod
    def main(cls):
        while True:
            menuUI = cls.menu()
            match menuUI:
                case 0:
                    cls.Inserir()
                case 1:
                    cls.Listar()
                case 2:
                    cls.Mais_Longa()
                case 3:
                    cls.Atualizar()
                case 4:
                    cls.Excluir()
                case 5:
                    cls.Mais_Rapida()
                case 6:
                    break
    @classmethod
    def Inserir(cls):
        cls.__contador += 1
        nome = input("Nome: ")
        data = input("Data da Corrida (DD/MM/AAAA): ")
        distancia = float(input("Distância: "))
        h,m,s = map(int,input().split(":"))
        tempo = timedelta(hours=h,minutes=m,seconds=s)
        Corrida = ControleCorrida(cls.__contador,nome,datetime.strptime(data, "%d/%m/%Y"),distancia,tempo)
        cls.__listacorrida.append(Corrida)
    @classmethod
    def Listar(cls):
        for i in cls.__listacorrida:
            print(i)
    @classmethod
    def Mais_Longa(cls):
        print(max(cls.__listacorrida, key=lambda t:t.get_duracao()))
        return
    @classmethod
    def Atualizar(cls):
        id = int(input("Informe o Identificador: "))
        for i in cls.__listacorrida:
            if id == i.get_id():
                newnome = input("novo nome: ")
                nova_data = input("nova data: ")
                nova_distancia= float(input("distancia: "))
                nova_duracao = input("nova duracao: ")
                i.set_name(newnome)
                i.set_distancia(nova_distancia)
                i.set_data(nova_data)
                i.set_duracao(nova_duracao)
                return "Deu certo"
            return "Deu errado"
    @classmethod
    def Excluir(cls):
        id = int(input("Informe o Identificador: "))
        for i in cls.__listacorrida:
            if id == i.get_id():
                cls.__listacorrida.remove(i)
    @classmethod
    def Mais_Rapida(cls):
        print(min(cls.__listacorrida, key=lambda t: t.get_duracao()).velocidade_media())
        return
ControleCorridaUI.main()