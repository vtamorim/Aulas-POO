import models

class View:
    @staticmethod
    def Cliente_Listar():
        return models.ClienteDAO.Listar()
    @staticmethod
    def Cliente_Inserir(nome,email,fone):
        models.ClienteDAO.Inserir(nome,email,fone)
    @staticmethod
    def Cliente_Atualizar(id,nome,email,fone):
        models.ClienteDAO.Atualizar(id,nome,email,fone)
    @staticmethod 
    def Cliente_Excluir(id):
        models.ClienteDAO.Excluir(id)