import random

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
    bingo = None  # atributo de classe

    @staticmethod
    def main():
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

    @staticmethod
    def mostrar_menu():
        print("\n--- MENU BINGO ---")
        print("1 - Iniciar novo jogo")
        print("2 - Sortear número")
        print("3 - Ver números sorteados")
        print("4 - Sair")
        print("Escolha uma opção: ", end='')

    @staticmethod
    def iniciar_jogo():
        try:
            num_bolas = int(input("Digite o número de bolas do bingo: "))
            if num_bolas <= 0:
                print("O número de bolas deve ser maior que zero.")
                return
        except ValueError:
            print("Valor inválido!")
            return
        BingoUI.bingo = Bingo()
        BingoUI.bingo.iniciar(num_bolas)
        print("Novo jogo iniciado!")

    @staticmethod
    def sortear():
        if BingoUI.bingo is None:
            print("Inicie um novo jogo primeiro!")
            return
        numero = BingoUI.bingo.sortear()
        if numero == -1:
            print("Todos os números já foram sorteados!")
        else:
            print(f"Número sorteado: {numero}")

    @staticmethod
    def sorteados():
        if BingoUI.bingo is None:
            print("Inicie um novo jogo primeiro!")
            return
        numeros = BingoUI.bingo.sorteados()
        if not numeros:
            print("Nenhum número sorteado ainda.")
        else:
            print("Números sorteados:", ", ".join(str(n) for n in numeros))
