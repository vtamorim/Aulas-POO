import view__  
from models import ContatoDAO, Contato

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
                    cls.Contato_Inserir()
                case 1:
                    cls.Contato_Listar()
                case 2:
                    cls.Contato_Atualizar()
                case 3:
                    cls.Contato_Excluir()
                case 4:
                    print("Saindo...")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    @classmethod
    def Contato_Inserir(cls):
        nome = input("Nome: ")
        email = input("Seu Email: ")
        fone = input("Seu fone: ")
        view__.Visualizador.Contato_Inserir(nome, email, fone)

    @classmethod
    def Contato_Listar(cls):
        view__.Visualizador.Contato_Listar()

    @classmethod
    def Contato_Atualizar(cls):
        id = int(input("ID do Contato a atualizar: "))
        view__.Visualizador.Cliente_Atualizar(id)

    @classmethod
    def Cliente_Excluir(cls):
        view__.Visualizador.Cliente_Excluir()


if __name__ == "__main__":
    UI.Main()
