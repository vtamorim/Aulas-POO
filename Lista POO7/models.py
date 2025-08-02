import json
import os

# Variável global para contar os IDs
contador = 0

class Cliente:
    def __init__(self, id, n, e, f):
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

    def set_id(self, newid):
        if not isinstance(newid, int) or newid <= 0:
            raise ValueError("Identificador Inválido")
        self.__id = newid
    def set_n(self, newn):
        if not isinstance(newn, str) or newn == "":
            raise ValueError("Nome Inválido")
        self.__n = newn
    def set_e(self, newe):
        if not isinstance(newe, str) or "@" not in newe:
            raise ValueError("Email Inválido")
        self.__e = newe
    def set_f(self, newf):
        if not isinstance(newf, str) or newf == "":
            raise ValueError("Fone inválido")
        self.__f = newf

    def __str__(self):
        return f"Identificador: {self.__id} Nome: {self.__n} Email: {self.__e} Fone: {self.__f}"

class ClienteDAO:
    __lista_cliente = []

    @classmethod
    def Inserir(cls, nome, email, fone):
        global contador
        contador += 1
        cliente = Cliente(contador, nome, email, fone)
        cls.__lista_cliente.append(cliente)
        print("Cliente inserido com sucesso!")

    @classmethod
    def Listar(cls):
        if not cls.__lista_cliente:
            print("Infelizmente você não tem nenhum cliente :( )")
        else:
            for cliente in cls.__lista_cliente:
                print(cliente)

    @classmethod
    def Listar_ID(cls):
        for cliente in cls.__lista_cliente:
            print(cliente.get_id())

    @classmethod
    def Atualizar(cls, id, *_):  # o *_ ignora os outros argumentos
        for cliente in cls.__lista_cliente:
            if cliente.get_id() == id:
                nome = input("Novo Nome do cliente: ")
                email = input("Novo Email do cliente: ")
                fone = input("Novo Telefone do cliente: ")
                cliente.set_n(nome)
                cliente.set_e(email)
                cliente.set_f(fone)
                print("Cliente atualizado com sucesso!")
                return
        print("Cliente não encontrado.")

    @classmethod
    def Excluir(cls):
        id = int(input("Identificador do cliente: "))
        for cliente in cls.__lista_cliente:
            if cliente.get_id() == id:
                print("Tem certeza que deseja excluir? S/N")
                if input().strip().upper() == "S":
                    cls.__lista_cliente.remove(cliente)
                    print("Cliente removido com sucesso!")
                return
        print("Cliente não encontrado.")

    @classmethod
    def Salvar(cls, filepath):
        with open(filepath, 'w') as file:
            json.dump([{
                "id": c.get_id(),
                "nome": c.get_n(),
                "email": c.get_e(),
                "fone": c.get_f(),
            } for c in cls.__lista_cliente], file, indent=4)

    @classmethod
    def Abrir(cls, filepath):
        global contador
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                lista = json.load(file)
                cls.__lista_cliente = [Cliente(d["id"], d["nome"], d["email"], d["fone"]) for d in lista]
                contador = max(d["id"] for d in lista)  # Atualiza contador para o último ID
                print("Dados carregados com sucesso!")
        else:
            cls.__lista_cliente = []
