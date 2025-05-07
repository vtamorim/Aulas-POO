question = int(input("Número da Questão: "))

match question:
    case 1:
        for i in range(1,10+1):
            print(i)
    case 2:
        lista = []
        for i in range(1,10+1):
            lista.append(i)
        lista.sort(reverse=True)
        print('\n'.join(lista))
    case 3:
        for i in range(1,10+1):
           if not i%3:
               print(-abs(i))
           else:
               print(i)
    case 4:
        for i in range(1,30+1):
            if not i%3:
                print(-abs(i))
            else:
                print(i)
    case 5:
        quantidade = 10  
        sequencia = [1]  

        for i in range(1, quantidade):
            proximo = sequencia[-1] + i
            sequencia.append(proximo)

        print("Resultado:", *sequencia)
    case 6:
        sequencia = []

        for i in range(1, 31, 3):
            trio = [i, i+1, i+2]
            soma = sum(trio)
            sequencia.extend(trio + [soma])  

        print("Resultado:", *sequencia)
