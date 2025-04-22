casos = int(input("Numero da Questão: "))
import math
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