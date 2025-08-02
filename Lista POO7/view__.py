import template

class Visualizador:
    @staticmethod
    def Cliente_Listar():
        template.ClienteDAO.Listar()

    @staticmethod
    def Cliente_Inserir(nome, email, fone):
        template.ClienteDAO.Inserir(nome, email, fone)

    @staticmethod
    def Cliente_Atualizar(id):
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        fone = input("Novo telefone: ")
        template.ClienteDAO.Atualizar(id, nome, email, fone)

    @staticmethod
    def Cliente_Excluir():
        template.ClienteDAO.Excluir()
