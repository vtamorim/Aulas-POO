from datetime import datetime,timedelta

class Treino:
    def __init__(self,id,dt,ds,t):
        self.__id = id
        self.__dt = dt
        self.__ds = ds
        self.__t = t

    def get_id(self):
        return self.__id
    def get__dt(self):
        return self.__dt
    def get__ds(self):
        return self.__ds
    def get_t(self):
        return self.__t

    def set_id(self,newid):
        if newid <= 0: raise ValueError("Identificador Inválido")
        self.__id = newid
    def set_dt(self,newdt):
        if newdt <= 0: raise ValueError("DT inválido")
        self.__dt = newdt
    def set_ds(self,newds):
        if newds <= 0: raise ValueError("DS inválido")
    def set_t(self,newt):
        if newt <=0: raise ValueError("T inválido ")

    def velocidade_media(self):
        return self.__ds/self.__t

    def __str__(self):
        return f"Identificador: {self.__id}\nData: {self.__dt}\nDistância: {self.__ds}\nTempo: {self.__t}"

class TreinoUI:
    __treinos = []
    __contador = 0
    @classmethod
    def Menu(cls):
        opcoes = ["Inserir","Listar","Listar_ID","Atualizar","Excluir","MaisRapido","Fim"]
        for i in range(len(opcoes)):
            print("[", i, "] ", opcoes[i])
        return int(input())
    @classmethod
    def Main(cls):
        while True:
            sla = TreinoUI.Menu()
            match sla:
                case 0:
                    pass
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
    @classmethod
    def Inserir(cls):
        contador += 1
        data = input("Data (00/00/0000):")
        distancia = float(input("Distância: "))
        h,m,s = map(int,input("Tempo do Treino: ").split(":"))
        tempo = timedelta(hours=h,minutes=m,seconds=s)
        treino = Treino(contador,data,distancia,tempo)
        cls.__treinos.append(treino)
    @classmethod
    def Listar(cls):
        for i in cls.__treinos:
            print(i)
    @classmethod
    def ListarID(cls):
        for i in cls.__treinos:
            print(i.get_id())
    @classmethod
    def Atualizar(cls):
        id = int(input("Identificador do Contato: "))
        for contato in cls.__treinos:
            if contato.get_id() == id:
                data = input("Nova data do Treino (00/00/0000): ")
                distancia = float(input("Nova Distancia do Treino: "))
                tempo  = input("Novo Tempo do Treino: ")
                contato.set_dt(data)
                contato.set_ds(distancia)
                contato.set_t(tempo)
                print("Contato atualizado com sucesso!")
                return
            print("Contato não encontrado.")
        
    @classmethod
    def Excluir(cls):
        id = int(input("Identificador do Treino: "))
        for contato in cls.__treinos:
            if contato.get_id() == id:
                print("Tem certeza que deseja excluir? S/N")
                if input().strip().upper() == "S":
                    cls.__treinos.remove(contato)
                    print("Treino removido com sucesso!")
                    return
                print("Treino não encontrado.")
    @classmethod
    def Mais_Rapido(cls):
        mr = cls.__treinos[0]
        for t in cls.__treinos:
            if t.velocidade_media() > mr.velocidade_media():
                mr = t
        print(mr)
        
    


