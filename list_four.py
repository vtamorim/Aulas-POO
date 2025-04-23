casos = int(input("Numero da Questão: "))
import math
import random
match casos:
    case 1:
        numeros = list(map(float, input().split()))
        delta = (numeros[1]**2) - (4 * numeros[0] * numeros[2])

        if numeros[0] == 0 or delta<0:
            print("Impossivel calcular")
        else:
            x1 = (-numeros[1] + math.sqrt(delta)) / (2 * numeros[0])
            x2 = (-numeros[1] - math.sqrt(delta)) / (2 * numeros[0])
            
            print(f"R1 = {x1:.5f}")
            print(f"R2 = {x2:.5f}")
    case 2:
        n1,n2 = list(map(int,input().split()))
        if n1 % n2 == 0 or n2 % n1 == 0:
            print("Sao Multiplos")
        else:
            print("Nao sao Multiplos")
    case 3:
        def identificar_animal(classe1, classe2, classe3):
            animais = {
                'vertebrado': {
                    'ave': {
                        'carnivoro': 'aguia',
                        'onivoro': 'pomba'
                    },
                    'mamifero': {
                        'onivoro': 'homem',
                        'herbivoro': 'vaca'
                    }
                },
                'invertebrado': {
                    'inseto': {
                        'hematofago': 'pulga',
                        'herbivoro': 'lagarta'
                    },
                    'anelideo': {
                        'hematofago': 'sanguessuga',
                        'onivoro': 'minhoca'
                    }
                }
            }

            return animais[classe1][classe2][classe3]

 
        classe1 = input().strip()  
        classe2 = input().strip()  
        classe3 = input().strip()  

        animal = identificar_animal(classe1, classe2, classe3)
        print(animal)

        verte_in = input().strip()
        type_an = input().strip()
        comir = input().strip()
        print(animal[verte_in][type_an][comir])
    case 4:
        ddd = {
            61: "Brasilia",
            71: "Salvador",
            11: "Sao Paulo",
            21: "Rio de Janeiro",
            32: "Juiz de Fora",
            19: "Campinas",
            27: "Vitoria",
            31: "Belo Horizonte"
        }

        number_ddd = int(input())
        if number_ddd in ddd:
            print(ddd[number_ddd])
        else:
            print("DDD não cadastrado")
    case 5:
        x,y = list(map(int,input().split()))
        x_cond = False
        y_cond = False
        for i in range(432+1):
            if i == x:
                x_cond = True
        for j in range(468+1):
            if j == y:
                y_cond = True
        if x_cond and y_cond:
            print("dentro")
        else:
            print("fora")
    case 6:
        
        A1 = int(input()) 
        A2 = int(input())  
        A3 = int(input()) 

        tempo1 = 0 * A1 + 2 * A2 + 4 * A3
        tempo2 = 2 * A1 + 0 * A2 + 2 * A3
        tempo3 = 4 * A1 + 2 * A2 + 0 * A3
        min_tempo = min(tempo1, tempo2, tempo3)

        print(min_tempo)
    case 7:
        max_valor = 100 + 1
        for i in range(1,max_valor):
            if i % 2 == 0:
                print(i)
    case 8:
        maior = -1
        posicao = -1

        for i in range(100):
            num = int(input())
            if num > maior:
                maior = num
                posicao = i + 1  

        print(maior)
        print(posicao)
    case 9:
        #experimentos = int(input())
        #for _ in range(1,experimentos + 1):
         #   pass
        sla = list(map(str,input().split()))
        sla[0] = int(sla[0])
        print(sla)
