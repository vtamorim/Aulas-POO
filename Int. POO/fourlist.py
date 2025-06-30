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
            __bingo = None  # atributo de classe

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
            @classmethod
            def Listar(cls):
                if len(cls.__lista_contato) <= 0: raise ValueError("Infelizmente você não tem nenhum contato :( )")
                print(cls.__lista_contato)  
            @classmethod
            def Atualizar(cls):
                id = int(input("Identificador do Contato: "))
                for i in cls.__lista_contato:
                    if i.__i == id:
                        nome = input("Novo Nome do Contato: ")
                        email = input("Novo Email do Contato: ")
                        fone  = input("Novo Telefone do Contato: ")
                        i.__n = nome
                        i.__e = email
                        i.__f = fone
                        print("Contato atualizado com sucesso!")
                    else:
                        raise ValueError("Erro ao Atualizar")
                
            @classmethod
            def Excluir(cls):
                id = int(input("Identificador do Contato: "))
                for i in cls.__lista_contato:
                    if i.__i == id:
                        print("Tem certeza que deseja excluir? S/N")
                        if input() == "S":
                            cls.__lista_contato.remove(i)
                    else:
                        raise ValueError("Erro ao Excluir o Contato")
                
                
            @classmethod
            def Pesquisar(cls):
                nome = input("Nome do Contato: ")
                for i in cls.__lista_contato:
                    if i.__n == nome:
                        print(i)
        if __name__ == "__main__":
            ContatoUI.Main()
    case 3:
        class Pais:
            def __init__(self,i,n,p,a):
                self.__i = i
                self.__p = p
                self.__n = n
                self.__a = a
            def get_nome(self):
                return self.__n
            
            def set_nome(self,nome):
                if nome == "": raise ValueError("Nome inválido")
                
            def set_id(self,id):
                if id <= 0: raise ValueError("Identificador Inválido")

            def set_p(self,pop):
                if pop <= 0: raise ValueError("População Inválida")

            def set_a(self,area):
                if area <=0: raise ValueError("Área inválida")

            def Densidade(self):
                return self.__p/self.__a
            def __str__(self):
                return f"Identificador: {self.__i} Nome: {self.__n} População: {self.__p} Área: {self.__a}"
        class PaisUI:
            __contatos = []
            @classmethod
            def Menu(cls):
                opcoes = ["Inserir","Atualizar","Excluir","Mostrar o mais Populoso","Mostrar o mais Povoado","Sair"]
                for i in range(len(opcoes)):
                    print("[", i ,"]", opcoes[i])
                return int(input())
            @classmethod
            def Main(cls):
                sla = 0
                while sla != 5:
                    sla = PaisUI.Menu()
                    if sla == 0: PaisUI.Inserir()
                    if sla == 1: PaisUI.Atualizar() 
                    if sla == 2: PaisUI.Excluir()
                    if sla == 3: PaisUI.M_Populoso()
                    if sla == 4: PaisUI.M_Povoado()
            @classmethod
            def Inserir(cls):
                id = int(input("Identificador: "))
                nome = input("Nome do País: ")
                pop = int(input("População do País: "))
                area = float(input("Área do País: "))
                p = Pais(id,nome,pop,area)
                cls.__contatos.append(p)
            @classmethod
            def Atualizar(cls):
                nome = input("Informe o seu nome: ")
                for i in cls.__contatos:
                    if i.get_nome().startswith(nome):
                        i.set_nome(input("Novo Nome: "))
                        i.set_id(int(input("Novo Identificador: ")))
                        i.set_p(int(input("Nova População: ")))
                        i.set_a(float(input("Nova Área: ")))
                        print(i)
            @classmethod
            def Excluir(cls):
                nome = input("Informe o seu nome: ")
                for i in cls.__contatos:
                    if i.get_nome().startswith(nome):
                        print(i)
                        cls.__contatos.remove(i)
                        print("Removido com sucesso")
            @classmethod
            def M_Populoso(cls):
                if not cls.__contatos:
                    print("Nenhum país cadastrado.")
                    return
                lista_nomes = []
                lista_popu = []
                for i in cls.__contatos:
                    lista_nomes.append(i.get_nome())
                    lista_popu.append(i._Pais__p)  
                print(f"Pais mais população: {lista_nomes[lista_popu.index(max(lista_popu))]}; População: {max(lista_popu)} ")

            @classmethod
            def M_Povoado(cls):
                if not cls.__contatos:
                    print("Nenhum país cadastrado.")
                    return
                lista_nomes = []
                lista_area = []
                for i in cls.__contatos:
                    lista_nomes.append(i.get_nome())
                    lista_area.append(i.Densidade())
                print(f"Pais mais povoado: {lista_nomes[lista_area.index(max(lista_area))]}; Densidade: {max(lista_area)} ")
        PaisUI.Main()