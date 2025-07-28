import json
import os
from datetime import datetime
contador = 0

class Contato:
    def __init__(self,i,n,e,f,d):
        self.__i = i
        self.__n = n
        self.__e = e
        self.__f = f 
        self.__d = d
    def set_nome(self,nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__n = nome
    def set_id(self,id):
        if id <= 0: raise ValueError("Identificador Inválido")
        self.__i = id
    def set_e(self,email):
        if email == "" or not "@" in email : raise ValueError("Email Inválido")
        self.__e = email
    def set_f(self,fone):
        if not fone.isdigit() or int(fone) <= 0: raise ValueError("Fone inválido")
        self.__f = fone
    def get_id(self):
        return self.__i
    def get_nome(self):
        return self.__n
    def get_mes(self):
        return self.__d.month
    def get_email(self):
        return self.__e
    def get_fone(self):
        return self.__f
    def get_nasci(self):
        return self.__d
    
    def __str__(self):
        return f"Identificador: {self.__i} Nome: {self.__n} Email: {self.__e} Fone: {self.__f} Nascimento: {self.__d}"

class ContatoUI:
    __lista_contato = []
    @classmethod
    def Menu(cls):
        opcoes = [
            "Inserir um Novo Contato","Listar os Contatos","Atualizar Dados do Contato","Excluir um Contato na Agenda","Pesquisar um Contato","Aniversariantes do Mês","Salvar contatos","Abrir contatos","Sair"
        ]
        for i in range(len(opcoes)):
            print("[", i ,"]", opcoes[i])
        return int(input())
    @classmethod
    def Main(cls):
        global contador
        while True:
            escolha = cls.Menu()
            match escolha:
                case 0:
                    cls.Inserir() 
                case 1:
                    cls.Listar()
                case 2:
                    cls.Atualizar()
                case 3:
                    cls.Excluir()
                case 4:
                    cls.Pesquisar()
                case 5:
                    cls.Aniversariantes()
                case 6:
                    filepath = input("Nome do arquivo para salvar (ex: contatos.json): ")
                    cls.Salvar(filepath)
                    print("Contatos salvos com sucesso!")
                case 7:
                    filepath = input("Nome do arquivo para abrir (ex: contatos.json): ")
                    cls.Abrir(filepath)
                    print("Contatos carregados com sucesso!")
                case 8:
                    print("Fim do Código")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
    @classmethod
    def Inserir(cls):
        global contador
        contador += 1
        nome = input("Nome do Contato: ")
        email = input("Email do Contato: ")
        fone  = input("Telefone do Contato: ")
        nascimento = input("Nascimento (ex: DD/MM/AAAA)")
        contato = Contato(contador,nome,email,fone,datetime.strptime(nascimento, "%d/%m/%Y") )
        cls.__lista_contato.append(contato)
        print("Contato inserido com sucesso!")
    @classmethod
    def Listar(cls):
        if not cls.__lista_contato:
            print("Infelizmente você não tem nenhum contato :( )")
        else:
            for contato in cls.__lista_contato:
                print(contato) 
    @classmethod
    def Listar_ID(cls):
        for i in range(1,contador+1):
            print(i)
    @classmethod
    def Atualizar(cls):
        id = int(input("Identificador do Contato: "))
        for contato in cls.__lista_contato:
            if contato.get_id() == id:
                nome = input("Novo Nome do Contato: ")
                email = input("Novo Email do Contato: ")
                fone  = input("Novo Telefone do Contato: ")
                contato.set_nome(nome)
                contato.set_e(email)
                contato.set_f(fone)
                print("Contato atualizado com sucesso!")
                return
        print("Contato não encontrado.")
    @classmethod
    def Excluir(cls):
        id = int(input("Identificador do Contato: "))
        for contato in cls.__lista_contato:
            if contato.get_id() == id:
                print("Tem certeza que deseja excluir? S/N")
                if input().strip().upper() == "S":
                    cls.__lista_contato.remove(contato)
                    print("Contato removido com sucesso!")
                return
        print("Contato não encontrado.")
    @classmethod
    def Pesquisar(cls):
        nome = input("Nome do Contato: ")
        encontrados = [c for c in cls.__lista_contato if c.get_nome() == nome]
        if encontrados:
            for c in encontrados:
                print(c)
        else:
            print("Contato não encontrado.")
    @classmethod
    def Aniversariantes(cls):
        mes = int(input("Mês para Informar: "))
        for contato in cls.__lista_contato:
            if contato.get_mes() == mes:
                print(contato) 
    @classmethod
    def Salvar(cls, filepath):
        with open(filepath, 'w') as file:
            json.dump([{
                "id": c.get_id(),
                "nome": c.get_nome(),
                "email": c.get_email(),
                "fone": c.get_fone(),
                "nascimento": c.get_nasci().strftime("%d/%m/%Y")
            } for c in cls.__lista_contato], file, indent=4)
    @classmethod
    def Abrir(cls, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                lista = json.load(file)
                cls.__lista_contato = [Contato(d["id"], d["nome"], d["email"], d["fone"], datetime.strptime(d["nascimento"], "%d/%m/%Y")) for d in lista]
                print(lista)
        else:
            cls.__lista_contato = []
if __name__ == "__main__":
    ContatoUI.Main()


