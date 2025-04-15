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
    