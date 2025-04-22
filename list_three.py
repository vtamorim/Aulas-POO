numero  = int(input("Número da Questão: "))
import math
match numero:
    case 1:
        primeiro = int(input("Primeiro Número: "))
        segundo = int(input("Segundo Número: "))
        PROD = primeiro * segundo
        print(f"PROD: {PROD}")
    case 2:
        primeiro = float(input("Primeiro Número: "))
        segundo  =float(input("Segundo Número: "))
        media = (primeiro + segundo)/ 2
        print(media)
    case 3:
        number= int(input("Numero: "))
        volume = (4/3) * math.pi * (number**3)
        print(volume)
    case 4:
        primeiro = int(input("Número 1: "))
        segundo = int(input("Número 2: "))
        print(primeiro % segundo)
    case 5:
        number_x = input("Valores de X (separar por espaço): ")
        number_y = input("Valores de Y (separar por espaço): ")
        number_x = number_x.split()
        number_y = number_y.split()
        print(math.sqrt(  (float(number_x[1]) - float(number_x[0]))**2 + (float(number_y[1] - float(number_y[0]))) **2  ))
        print(int (number_y[1]))
    case 6:
        numbers = input("")
        numbers = numbers.split()
        numbers = [float(x) for x in numbers]
        if len(numbers) > 4:
            quit("Questões de Números Inválidos")
        for i in numbers:
            if 2 > i > 6:
                quit("Número Inválido")
        print(sum(numbers) - 3)
        