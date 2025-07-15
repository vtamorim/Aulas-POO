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
        if self.__t.total_seconds() == 0:
            return 0
        return self.__ds / self.__t.total_seconds()

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
                    cls.Inserir()
                case 1:
                    cls.Listar()
                case 2:
                    cls.ListarID()
                case 3:
                    cls.Atualizar()
                case 4:
                    cls.Excluir()
                case 5:
                    cls.Mais_Rapido()
                case 6:
                    print("Fim do Programa")
                    break
                case _:
                    print("Opção Inválida, tente novamente.")
    @classmethod
    def Inserir(cls):
        cls.__contador += 1
        data = input("Data (00/00/0000):")
        distancia = float(input("Distância: "))
        h,m,s = map(int,input("Tempo do Treino: ").split(":"))
        tempo = timedelta(hours=h,minutes=m,seconds=s)
        treino = Treino(cls.__contador,data,distancia,tempo)
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
        if not cls.__treinos:
            print("Nenhum treino cadastrado.")
            return
        treino_rapido = min(cls.__treinos, key=lambda t: t.get_t())
        print(f"Treino mais rápido:\n{treino_rapido}\nVelocidade média: {treino_rapido.velocidade_media():.2f} m/s")
        
TreinoUI.Main()
print("Fim do Programa")