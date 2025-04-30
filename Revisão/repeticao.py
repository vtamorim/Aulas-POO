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
        pass