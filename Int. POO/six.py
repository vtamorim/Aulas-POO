import json
import os
from datetime import datetime
contador = 0
number= input("Numero da questão: ")
match number:
    case "1":
        class Cliente:
            def __init__(self,i,n,e,f):
                self.__i = i
                self.__n = n
                self.__e = e
                self.__f = f
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
            def get_email(self):
                return self.__e
            def get_fone(self):
                return self.__f
            def __str__(self):
                return f"Identificador: {self.__i} Nome: {self.__n} Email: {self.__e} Fone: {self.__f}"
        
        class ClienteUI:
            __lista_Cliente = []
            @classmethod
            def Menu(cls):
                opcoes = [
                    "Inserir um Novo Cliente",
                    "Listar os Clientes",
                    "Atualizar Dados do Cliente",
                    "Excluir um Cliente na Agenda",
                    "Pesquisar um Cliente",
                    "Salvar clientes",
                    "Abrir clientes",
                    "Sair"
                ]
                for i in range(len(opcoes)):
                    print("[", i ,"]", opcoes[i])
                return int(input())
            @classmethod
            def Main(cls):
                global contador
                while True:
                    escolha = ClienteUI.Menu()
                    match escolha:
                        case 0:
                            ClienteUI.Inserir() 
                        case 1:
                            ClienteUI.Listar()
                        case 2:
                            ClienteUI.Atualizar()
                        case 3:
                            ClienteUI.Excluir()
                        case 4:
                            ClienteUI.Pesquisar()
                        case 5:
                            filepath = input("Nome do arquivo para salvar (ex: clientes.json): ")
                            ClienteUI.Salvar(filepath)
                            print("Clientes salvos com sucesso!")
                        case 6:
                            filepath = input("Nome do arquivo para abrir (ex: clientes.json): ")
                            ClienteUI.Abrir(filepath)
                            print("Clientes carregados com sucesso!")
                        case 7:
                            print("Fim do Código")
                            break
            @classmethod
            def Inserir(cls):
                global contador
                contador += 1
                nome = input("Nome do Cliente: ")
                email = input("Email do Cliente: ")
                fone  = input("Telefone do Cliente: ")
                cliente = Cliente(contador,nome,email,fone)
                cls.__lista_Cliente.append(cliente)
                print("Cliente inserido com sucesso!")
            @classmethod
            def Listar(cls):
                if not cls.__lista_Cliente:
                    print("Infelizmente você não tem nenhum Cliente :( )")
                else:
                    for Cliente in cls.__lista_Cliente:
                        print(Cliente)
            @classmethod
            def Listar_ID(cls):
                for i in range(1,contador+1):
                    print(i)

            @classmethod
            def Atualizar(cls):
                id = int(input("Identificador do Cliente: "))
                for Cliente in cls.__lista_Cliente:
                    if Cliente.get_id() == id:
                        nome = input("Novo Nome do Cliente: ")
                        email = input("Novo Email do Cliente: ")
                        fone  = input("Novo Telefone do Cliente: ")
                        Cliente.set_nome(nome)
                        Cliente.set_e(email)
                        Cliente.set_f(fone)
                        print("Cliente atualizado com sucesso!")
                        return
                print("Cliente não encontrado.")
            @classmethod
            def Excluir(cls):
                id = int(input("Identificador do Cliente: "))
                for Cliente in cls.__lista_Cliente:
                    if Cliente.get_id() == id:
                        print("Tem certeza que deseja excluir? S/N")
                        if input().strip().upper() == "S":
                            cls.__lista_Cliente.remove(Cliente)
                            print("Cliente removido com sucesso!")
                        return
                print("Cliente não encontrado.")
            @classmethod
            def Pesquisar(cls):
                nome = input("Nome do Cliente: ")
                encontrados = [c for c in cls.__lista_Cliente if c.get_nome() == nome]
                if encontrados:
                    for c in encontrados:
                        print(c)
                else:
                    print("Cliente não encontrado.")
            @classmethod
            def Salvar(cls, filepath):
                
                with open(filepath, 'w') as file:
                    json.dump([{
                        "id": c.get_id(),
                        "nome": c.get_nome(),
                        "email": c.get_email(),
                        "fone": c.get_fone()
                    } for c in cls.__lista_Cliente], file, indent=4)

            @classmethod
            def Abrir(cls, filepath):
                if os.path.exists(filepath):
                    with open(filepath, 'r') as file:
                        lista = json.load(file)
                        cls.__lista_Cliente = [Cliente(d["id"], d["nome"], d["email"], d["fone"]) for d in lista]
                        print(lista)
                else:
                    cls.__lista_Cliente = []

        if __name__ == "__main__":
            ClienteUI.Main()
    case 2:
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
                opcoes = ["Inserir um Novo Contato","Listar os Contatos","Atualizar Dados do Contato","Excluir um Contato na Agenda","Pesquisar um Contato","Aniversariantes","Sair"]
                for i in range(len(opcoes)):
                    print("[", i ,"]", opcoes[i])
                return int(input())
            @classmethod
            def Main(cls):
                global contador
                while True:
                    escolha = ContatoUI.Menu()
                    match escolha:
                        case 0:
                            ContatoUI.Inserir() 
                        case 1:
                            ContatoUI.Listar()
                        case 2:
                            ContatoUI.Atualizar()
                        case 3:
                            ContatoUI.Excluir()
                        case 4:
                            ContatoUI.Pesquisar()
                        case 5:
                            ContatoUI.Aniversariantes()
                        case 6:
                            print("Fim do Código")
                            break
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
        if __name__ == "__main__":
            ContatoUI.Main()























        
"""
    @staticmethod
    def load_table(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_table(file_path, table):
        with open(file_path, 'w') as file:
            json.dump(table, file, indent=4)

    @staticmethod
    def inserir(name, password, table, file_path):
        if name in table:
            return "Error: Nickname already exists."
        table[name] = password
        Nickname.save_table(file_path, table)
        return "Nickname inserted successfully."

    @staticmethod
    def delet(name, table, file_path):
        if name in table:
            del table[name]
            Nickname.save_table(file_path, table)
            return "Nickname deleted successfully."
        return "Error: Nickname not found."

    @staticmethod
    def search(name, table):
        return name in table

    @staticmethod
    def update(name, table, file_path):
        if name in table:
            new_name = input("New nickname: ")
            if new_name in table:
                return "Error: New nickname already exists."
            table[new_name] = table.pop(name)
            Nickname.save_table(file_path, table)
            return "Nickname updated successfully."
        return "Error: Nickname not found."

    @staticmethod
    def view_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                print(json.dumps(data, indent=4)) 
        else:
            print("Arquivo JSON não encontrado.")

def interaction(table, file_path):
    options = ['Insert', 'Delete', 'Search', 'Update', 'View JSON']
    for index, element in enumerate(options):
        print(f"[{index}] {element}")
    try:
        chosen = int(input("Choose an option: "))
        if chosen not in range(len(options)):
            print("Invalid option.")
            return table
    except ValueError:
        print("Invalid input. Please enter a number.")
        return table

    nick = input("Nickname: ")
    if chosen != 2:  
        password = input("Password: ")

    if chosen == 0:
        print(Nickname.inserir(nick, password, table, file_path))
    elif chosen == 1:
        print(Nickname.delet(nick, table, file_path))
    elif chosen == 2:
        exists = Nickname.search(nick, table)
        print("Nickname found." if exists else "Nickname not found.")
    elif chosen == 3:
        print(Nickname.update(nick, table, file_path))
    elif chosen == 4: 
        Nickname.view_json(file_path)

    return table


def main():
    file_path = 'table.json'
    table = Nickname.load_table(file_path)

    while True:
        interaction(table, file_path)


if __name__ == '__main__':
    main()
"""
