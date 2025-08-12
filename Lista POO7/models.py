import json,os
contador = 0


class Cliente:
    def __init__(self,id,n,e,f):
        self.__id = id
        self.__n = n
        self.__e = e 
        self.__f = f

    def get_id(self):
        return self.__id
    def get_n(self):
        return self.__n
    def get_e(self):
        return self.__e
    def get_f(self):
        return self.__f
    
    def set_id(self,newid):
        if not isinstance(newid,int): raise ValueError("Erro '-' ")
        self.__id = newid
    def set_n(self,newn):
        if not isinstance(newn,str): raise  ValueError("Erro ,-, ")
        self.__n = newn
    def set_e(self,newe):
        if not isinstance(newe,str) or "@" not in newe: raise ValueError("Erro")
        self.__e = newe
    def set_f(self,newf):
        if not isinstance(newf,str): raise ValueError("sla")

    def __str__(self):
        return f"Id: {self.__id} nome: {self.__n} email: {self.__e} fone: {self.__f}"
    
class ClienteDAO:
    __objetos = []
    __lista_id=  []
    @classmethod
    def Inserir(cls,nome,email,fone):
        global contador
        contador +=1
        cliente = Cliente(contador,nome,email,fone)
        cls.__objetos.append(cliente)
    @classmethod
    def Listar(cls):
        for i in cls.__objetos:
            print(i) 
    @classmethod
    def Listar_id(cls):
        for i in cls.__objetos:
            print(i.get_id())
    @classmethod
    def Atualizar(cls,id,nome,email,fone):
        for i in cls.__objetos:
            if id == i.get_id():
                i.set_n(nome)
                i.set_e(email)
                i.set_f(fone)
    @classmethod
    def Excluir(cls,id):
        for i in cls.__objetos:
            if id == i.get_id():
                cls.__objetos.remove(i)
    @classmethod
    def Abrir(cls,filepath):
        global contador
        if os.path.exists(filepath):
            with open(filepath,"r") as file:
                lista = json.load(file)
                cls.__objetos = [Cliente(d["id"],d["n"], d["e"],d["f"]) for d in lista]
            contador = max(d["id"] for d in lista)
    @classmethod
    def Salvar(cls,filepath):
        with open(filepath,"w") as file:
            json.dump([{
                "id": i.get_id(),
                "nome": i.get_n(),
                "email": i.get_e(),
                "fone": i.get_f()
            }
                for i in cls.__objetos
            ], file,indent=4) 