numero_questao = int(input("Número da Questão: "))

import math
match numero_questao:
    case 1:
        name = input("Seu nome: ")
        indice = name.find(' ')
        print(f'Bem-vindo(a) ao Python: {name[:indice]}')
    case 2:
        nota_first = int(input("Nota do Primeiro Bimestre: "))
        nota_second = int(input("Nota do Segundo Bimestre: "))
        media = ((nota_first * 2) + (nota_second * 3)) //5
        print(media)
    case 3:
        base = int(input("Base de um Triângulo"))
        altura = int(input("Altura de um Triângulo: "))
        print(base*altura)
        print((base*2) + (altura*2))
        print(math.sqrt(base**2 + altura**2))
    case 4:
        frase = input("Uma frase: ")
        indice = frase.rfind(' ')
        print(frase[indice +1:])