question = int(input("Número da Questão: "))

match question:
    case 1:
        print("Digite dois valores inteiros")
        n1 = int(input())
        n2 = int(input())
        print(f"Maior = {max(n1,n2)}")
    case 2:
        print("Digite quatro valores inteiros")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        n4 = int(input())
        lista = [n1,n2,n3,n4]
        media = sum(lista) / 4
        print(f"Média = {media}")
        print("Números menores que a média")
        lista_max = []
        for i in lista:
            if i <= media:
                print(i)
            else:
                lista_max.append(i)
        print("Números maiores que à média")
        print('\n'.join(str(v) for v in lista_max))
    case 3:
        print("Digite quatro valores inteiros")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        n4 = int(input())
        lista= [n1,n2,n3,n4]
        lista_par = []
        lista_impar = []
        for i in lista:
            if not i%2:
                lista_par.append(i)
            else:
                lista_impar.append(i)

        print(f"Soma do pares = {sum(lista_par)}")
        print(f"Soma do ímpares = {sum(lista_impar)}")
    case 4:
        