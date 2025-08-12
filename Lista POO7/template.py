import view__
from models import ClienteDAO, Cliente
class UI:
    @classmethod
    def Menu(cls):
            opcoes = [
                "Inserir um Novo Cliente",
                "Listar os Clientes",
                "Atualizar Dados do Cliente",
                "Excluir um Cliente na Agenda",
                "Sair"
            ]
            for i in range(len(opcoes)):
                print("[", i, "]", opcoes[i])
            return int(input("Escolha uma opção: "))

    @classmethod
    def Main(cls):
            while True:
                escolha = cls.Menu()
                match escolha:
                    case 0:
                        cls.Cliente_Inserir()
                    case 1:
                        cls.Cliente_Listar()
                    case 2:
                        cls.Cliente_Atualizar()
                    case 3:
                        cls.Cliente_Excluir()
                    case 4:
                        print("Saindo...")
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")
    @classmethod
    def Cliente_Listar(cls):
        view__.View.Cliente_Listar()
    @staticmethod
    def Cliente_Inserir():
        nome = input()
        email = input()
        fone = input()
        view__.View.Cliente_Inserir(nome,email,fone)
    @staticmethod
    def Cliente_Atualizar():
         id = int(input("Informe o id"))
         novo_nome = input()
         novo_email = input()
         novo_fone = input()
         view__.View.Cliente_Atualizar(id,novo_nome,novo_email,novo_fone)
    @staticmethod
    def Cliente_Excluir():
         id = int(input("Identificador:"))
         view__.View.Cliente_Excluir(id)
        
UI.Main()