from datetime import datetime
from enum import Enum

number = int(input("Numero da Questão: "))
match number:
    case 1:
        class Paciente:
            def __init__(self,nome,cpf,telefone, nasc):
                self.__n = nome
                self.__c = cpf
                self.__t = telefone
                self.__nasc = nasc

            def get_nome(self):
                return self.__n

            def get_cpf(self):
                return self.__c

            def get_telefone(self):
                return self.__t
            
            def get_nascimento(self):
                return self.__nasc


            def set_nome(self,nome):
                if nome == "": raise ValueError("")
                self.__n = nome
            
            def set_cpf(self,cpf):
                if cpf == "": raise ValueError("")
                self.__c = cpf
            
            def set_telefone(self,telefone):
                if telefone <= 0: raise ValueError("")
                self.__t = telefone

            def set_nascimento(self,nascimento):
                self.__n = nascimento


            def Idade(self):
                tempo = datetime.now() - datetime.strptime(self.__nasc, "%d/%m/%Y")
                return f"Ano: {tempo.days // 365} Meses: {tempo.days % 365 // 30}"
            def __str__(self):
                return f"Nome: {self.__n} CPF: {self.__c} Telefone: {self.__t} Nascimento: {self.__n}"
            
        class PacienteUI:
            @staticmethod
            def menu():
                opcoes = ["Cadastro","Sair"]
                for i in range(len(opcoes)):
                    print(i, opcoes[i])
                return int(input())
            @staticmethod
            def main():
                while True:
                            escolha = PacienteUI.menu()
                            match escolha:
                                case 0:
                                    PacienteUI.Cadastro_dados() 
                                case 1:
                                    print("Fim do Código")
                                    break
            @staticmethod
            def Cadastro_dados():

                nome = input("n: ")
                cpf = input("cpf: ")
                telefone = int(input("telefone: "))
                nascimento = input("nasicmento: ")

                qualquercoisa = Paciente(nome,cpf,telefone,nascimento)
                print(qualquercoisa.__str__())
                print(qualquercoisa.Idade())



        PacienteUI.main()
    case 2:
        class Boleto:
            def __init__(self, cod, emissao, venci, valor):
                self.__cod = cod
                self.__emissao = emissao
                self.__venci = venci
                self.__valor = valor
                self.__valorpago = 0

            def set_cod(self,cod):
                if cod == "": raise ValueError
                self.__cod = cod

            def set_emissao(self,emissao):
                self.__emissao = emissao

            def set_venci(self,venci):
                self.__venci = venci

            def set_valor(self,valor):
                if valor <= 0: raise ValueError
                self.__valor = valor

            def Pagar(self,valorpago):
                if valorpago > self.__valor: raise ValueError("Erro cara '-'")
                self.__valorpago = valorpago
            def Situacao(self):
                if self.__valorpago == 0: return Pagamento(0)
                elif self.__valorpago < self.__valor: return Pagamento(1)
                else: return Pagamento(2)

            def __str__(self):
                return f"{self.__cod} {self.__emissao} {self.__valor} {self.__valorpago} {self.__venci}"
            
        class Pagamento(Enum):
            EmAberto = 0
            PagoParcial = 1
            Pago = 2
        
        class BoletoUI:
            @staticmethod
            def menu():
                opcoes = ["Cadastro","Sair"]
                for i in range(len(opcoes)):
                    print(i, opcoes[i])
                return int(input())
            @staticmethod
            def main():
                while True:
                            escolha = PacienteUI.menu()
                            match escolha:
                                case 0:
                                    PacienteUI.Cadastro_dados() 
                                case 1:
                                    print("Fim do Código")
                                    break
            @staticmethod
            def Cadastro_dados():

                codigo_barras = input("codigo : ")
                emissao = input("cpf: ")
                venci = input("venci: ")
                valor = float(input("nasicmento: "))

                qualquercoisa = Boleto(codigo_barras,emissao,venci,valor)
                print(qualquercoisa.Pagar(float(input("Pagar: "))))
                print(qualquercoisa.Situacao())
                print(qualquercoisa.__str__())
    case 3:
        class Contato:
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
        
        class ContatoUI:
            __lista_contato = []
            @classmethod
            def Menu(cls):
                opcoes = ["Inserir um Novo Contato","Listar os Contatos","Atualizar Dados do Contato","Excluir um Contato na Agenda","Pesquisar um Contato","Sair"]
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
                            print("Fim do Código")
                            break
            @classmethod
            def Inserir(cls):
                global contador
                contador += 1
                nome = input("Nome do Contato: ")
                email = input("Email do Contato: ")
                fone  = input("Telefone do Contato: ")
                contato = Contato(contador,nome,email,fone)
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
        if __name__ == "__main__":
            ContatoUI.Main()
                
