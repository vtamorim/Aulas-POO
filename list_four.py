casos = int(input("Numero da Questão"))
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


