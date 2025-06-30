import random
contador = 0

print("Escolha uma das opções abaixo:")
escolha = int(input("Número da Questão: "))
match escolha:
    case 1:
        class Bingo:
            def __init__(self):
                self.num_bolas = 0
                self.bolas_sorteadas = []
                self.bolas_restantes = []

            def iniciar(self, num_bolas):
                self.num_bolas = num_bolas
                self.bolas_sorteadas = []
                self.bolas_restantes = list(range(1, num_bolas + 1))

            def sortear(self):
                if not self.bolas_restantes:
                    return -1  
                bola = random.choice(self.bolas_restantes)
                self.bolas_restantes.remove(bola)
                self.bolas_sorteadas.append(bola)
                return bola

            def sorteados(self):
                return self.bolas_sorteadas.copy()

        class BingoUI:
            __bingo = None

            @classmethod
            def main(cls):
                while True:
                    BingoUI.mostrar_menu()
                    try:
                        opcao = int(input())
                    except ValueError:
                        print("Opção inválida!")
                        continue

                    if opcao == 1:
                        BingoUI.iniciar_jogo()
                    elif opcao == 2:
                        BingoUI.sortear()
                    elif opcao == 3:
                        BingoUI.sorteados()
                    elif opcao == 4:
                        print("Saindo...")
                        break
                    else:
                        print("Opção inválida!")

            @classmethod
            def mostrar_menu(cls):
                print("\n--- MENU BINGO ---")
                print("1 - Iniciar novo jogo")
                print("2 - Sortear número")
                print("3 - Ver números sorteados")
                print("4 - Sair")
                print("Escolha uma opção: ", end='')

            @classmethod
            def iniciar_jogo(cls):
                try:
                    num_bolas = int(input("Digite o número de bolas do bingo: "))
                    if num_bolas <= 0:
                        print("O número de bolas deve ser maior que zero.")
                        return
                except ValueError:
                    print("Valor inválido!")
                    return
                cls.__bingo = Bingo()
                cls.__bingo.iniciar(num_bolas)
                print("Novo jogo iniciado!")

            @classmethod
            def sortear(cls):
                if  cls.__bingo is None:
                    print("Inicie um novo jogo primeiro!")
                    return
                numero = cls.__bingo.sortear()
                if numero == -1:
                    print("Todos os números já foram sorteados!")
                else:
                    print(f"Número sorteado: {numero}")

            @classmethod
            def sorteados(cls):
                if cls.__bingo is None:
                    print("Inicie um novo jogo primeiro!")
                    return
                numeros = cls.__bingo.sorteados()
                if not numeros:
                    print("Nenhum número sorteado ainda.")
                else:
                    print("Números sorteados:", ", ".join(str(n) for n in numeros))
        if __name__ == "__main__":
            BingoUI.main()
    case 2:
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
    case 3:
        class Pais:
            def __init__(self,i,n,p,a):
                self.__i = i
                self.__p = p
                self.__n = n
                self.__a = a
            def get_id(self):
                return self.__i
            def get_nome(self):
                return self.__n
            def get_populacao(self):
                return self.__p
            def get_area(self):
                return self.__a
            def set_nome(self,nome):
                if nome == "": raise ValueError("Nome inválido")
                self.__n = nome
            def set_id(self,id):
                if id <= 0: raise ValueError("Identificador Inválido")
                self.__i = id
            def set_p(self,pop):
                if pop <= 0: raise ValueError("População Inválida")
                self.__p = pop
            def set_a(self,area):
                if area <=0: raise ValueError("Área inválida")
                self.__a = area
            def Densidade(self):
                return self.__p/self.__a
            def __str__(self):
                return f"Identificador: {self.__i} Nome: {self.__n} População: {self.__p} Área: {self.__a}"
        class PaisUI:
            __contatos = []
            @classmethod
            def Menu(cls):
                opcoes = ["Inserir","Atualizar","Excluir","Mostrar o mais Populoso","Mostrar o mais Povoado","Listar Países","Sair"]
                for i in range(len(opcoes)):
                    print("[", i ,"]", opcoes[i])
                return int(input())
            @classmethod
            def Main(cls):
                sla = 0
                while sla != 6:
                    sla = PaisUI.Menu()
                    if sla == 0: PaisUI.Inserir()
                    elif sla == 1: PaisUI.Atualizar() 
                    elif sla == 2: PaisUI.Excluir()
                    elif sla == 3: PaisUI.M_Populoso()
                    elif sla == 4: PaisUI.M_Povoado()
                    elif sla == 5: PaisUI.Listar()
                    elif sla == 6: 
                        print("Fim do Código")
                        break
            @classmethod
            def Inserir(cls):
                id = int(input("Identificador: "))
                nome = input("Nome do País: ")
                pop = int(input("População do País: "))
                area = float(input("Área do País: "))
                p = Pais(id,nome,pop,area)
                cls.__contatos.append(p)
                print("País inserido com sucesso!")
            @classmethod
            def Atualizar(cls):
                nome = input("Informe o nome do país: ")
                for i in cls.__contatos:
                    if i.get_nome().startswith(nome):
                        i.set_nome(input("Novo Nome: "))
                        i.set_id(int(input("Novo Identificador: ")))
                        i.set_p(int(input("Nova População: ")))
                        i.set_a(float(input("Nova Área: ")))
                        print("País atualizado:", i)
                        return
                print("País não encontrado.")
            @classmethod
            def Excluir(cls):
                nome = input("Informe o nome do país: ")
                for i in cls.__contatos:
                    if i.get_nome().startswith(nome):
                        print(i)
                        cls.__contatos.remove(i)
                        print("Removido com sucesso")
                        return
                print("País não encontrado.")
            @classmethod
            def M_Populoso(cls):
                if not cls.__contatos:
                    print("Nenhum país cadastrado.")
                    return
                mais_populoso = max(cls.__contatos, key=lambda p: p.get_populacao())
                print(f"País mais populoso: {mais_populoso.get_nome()}; População: {mais_populoso.get_populacao()}")
            @classmethod
            def M_Povoado(cls):
                if not cls.__contatos:
                    print("Nenhum país cadastrado.")
                    return
                mais_povoado = max(cls.__contatos, key=lambda p: p.Densidade())
                print(f"País mais povoado: {mais_povoado.get_nome()}; Densidade: {mais_povoado.Densidade()}")
            @classmethod
            def Listar(cls):
                if not cls.__contatos:
                    print("Nenhum país cadastrado.")
                else:
                    for p in cls.__contatos:
                        print(p)
        PaisUI.Main()