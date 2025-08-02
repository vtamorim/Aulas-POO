import view__  
from models import ClienteDAO, Cliente

class UI:
    @classmethod
    def Menu(cls):
        opcoes = [
            "Inserir um Novo Contato",
            "Listar os Contatos",
            "Atualizar Dados do Contato",
            "Excluir um Contato na Agenda",
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
    def Cliente_Inserir(cls):
        nome = input("Nome: ")
        email = input("Seu Email: ")
        fone = input("Seu fone: ")
        view__.Visualizador.Cliente_Inserir(nome, email, fone)

    @classmethod
    def Cliente_Listar(cls):
        view__.Visualizador.Cliente_Listar()

    @classmethod
    def Cliente_Atualizar(cls):
        id = int(input("ID do cliente a atualizar: "))
        view__.Visualizador.Cliente_Atualizar(id)

    @classmethod
    def Cliente_Excluir(cls):
        view__.Visualizador.Cliente_Excluir()


if __name__ == "__main__":
    UI.Main()
