from datetime import datetime
from enum import Enum
contador = 0
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
                tempo = datetime.now() - self.__nasc
                return f"Ano: {tempo.days // 365} Meses: {tempo.days % 365 // 30}"
            def __str__(self):
                return f"Nome: {self.__n} CPF: {self.__c} Telefone: {self.__t} Nascimento: {self.__nasc}"
            
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

                qualquercoisa = Paciente(nome,cpf,telefone,datetime.strptime(nascimento, "%d/%m/%Y"))
                print(qualquercoisa.__str__())
                print(qualquercoisa.Idade())



        PacienteUI.main()
    case 2:

        class Pagamento(Enum):
            EmAberto = 0
            PagoParcial = 1
            Pago = 2

        class Boleto:
            def __init__(self, cod_barras: str, data_emissao: datetime, data_vencimento: datetime, valor_boleto: float):
                self.cod_barras = cod_barras
                self.data_emissao = data_emissao
                self.data_vencimento = data_vencimento
                self.valor_boleto = valor_boleto
                self.data_pagamento = None
                self.valor_pago = 0.0
                self.situacao_pagamento = Pagamento.EmAberto

            def pagar(self, valor: float, data: datetime = None):
                self.valor_pago += valor
                self.data_pagamento = data or datetime.now()

                if self.valor_pago == 0:
                    self.situacao_pagamento = Pagamento.EmAberto
                elif self.valor_pago < self.valor_boleto:
                    self.situacao_pagamento = Pagamento.PagoParcial
                else:
                    self.situacao_pagamento = Pagamento.Pago

            def get_situacao(self):
                return self.situacao_pagamento

            def __str__(self):
                return (f"Código de Barras: {self.cod_barras}\n"
                        f"Data de Emissão: {self.data_emissao.strftime('%d/%m/%Y')}\n"
                        f"Data de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n"
                        f"Valor do Boleto: R$ {self.valor_boleto:.2f}\n"
                        f"Valor Pago: R$ {self.valor_pago:.2f}\n"
                        f"Situação: {self.situacao_pagamento.name}\n"
                        f"Data de Pagamento: {self.data_pagamento.strftime('%d/%m/%Y %H:%M') if self.data_pagamento else '---'}")

        class BoletoUI:
            __lista_boletos = []
            __contador = 0

            @classmethod
            def menu(cls):
                opcoes = [
                    "Criar novo boleto",
                    "Listar boletos",
                    "Pagar um boleto",
                    "Ver situação de um boleto",
                    "Sair"
                ]
                for i, op in enumerate(opcoes):
                    print(f"[{i}] {op}")
                return int(input("Escolha uma opção: "))

            @classmethod
            def main(cls):
                while True:
                    escolha = cls.menu()
                    match escolha:
                        case 0:
                            cls.criar_boleto()
                        case 1:
                            cls.listar_boletos()
                        case 2:
                            cls.pagar_boleto()
                        case 3:
                            cls.ver_situacao()
                        case 4:
                            print("Saindo...")
                            break
                        case _:
                            print("Opção inválida.")

            @classmethod
            def criar_boleto(cls):
                cls.__contador += 1
                cod_barras = input("Código de barras: ")
                emissao = datetime.strptime(input("Data de emissão (DD/MM/AAAA): "), "%d/%m/%Y")
                vencimento = datetime.strptime(input("Data de vencimento (DD/MM/AAAA): "), "%d/%m/%Y")
                valor = float(input("Valor do boleto: "))
                boleto = Boleto(cod_barras, emissao, vencimento, valor)
                cls.__lista_boletos.append(boleto)
                print("Boleto criado com sucesso!")

            @classmethod
            def listar_boletos(cls):
                if not cls.__lista_boletos:
                    print("Nenhum boleto cadastrado.")
                else:
                    for i, boleto in enumerate(cls.__lista_boletos):
                        print(f"\n[ID {i}] --------------------")
                        print(boleto)

            @classmethod
            def pagar_boleto(cls):
                if not cls.__lista_boletos:
                    print("Nenhum boleto para pagar.")
                    return
                id = int(input("Digite o ID do boleto que deseja pagar: "))
                if 0 <= id < len(cls.__lista_boletos):
                    valor = float(input("Valor a pagar: "))
                    cls.__lista_boletos[id].pagar(valor)
                    print("Pagamento registrado.")
                else:
                    print("ID inválido.")

            @classmethod
            def ver_situacao(cls):
                if not cls.__lista_boletos:
                    print("Nenhum boleto cadastrado.")
                    return
                id = int(input("Digite o ID do boleto: "))
                if 0 <= id < len(cls.__lista_boletos):
                    print(f"Situação: {cls.__lista_boletos[id].get_situacao().name}")
                else:
                    print("ID inválido.")

        # Executar interface
        if __name__ == "__main__":
            BoletoUI.main()

    case 3:
        class Contato:
            def __init__(self,i,n,e,f,d):
                self.__i = i
                self.__n = n
                self.__e = e
                self.__f = f 
                self.__d = datetime.strptime(d, "%d/%m/%Y") 
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
                contato = Contato(contador,nome,email,fone,nascimento)
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
                
