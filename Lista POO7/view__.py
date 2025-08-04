import template

class Visualizador:
    @staticmethod
    def Contato_Listar():
        template.ContatoDAO.Listar()

    @staticmethod
    def Contato_Inserir(nome, email, fone):
        template.ContatoDAO.Inserir(nome, email, fone)

    @staticmethod
    def Contato_Atualizar(id):
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")
        template.ContatoDAO.Atualizar(id, nome, email, fone)

    @staticmethod
    def Contato_Excluir():
        template.ContatoDAO.Excluir()
