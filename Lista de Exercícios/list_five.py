numero = int(input("Número da Questão: "))

match numero:

    case 1:
        def maior(a,b):
            return max(a,b)

        one_number = int(input("Primeiro: "))

        second_number = int(input("Segundo: "))


        maior(one_number,second_number)
    case 2:
        def maior(a,b,c):
            return max(a,b,c)

        one_number = int(input("Primeiro: "))

        second_number = int(input("Segundo: "))

        three_number = int(input("Terceiro; "))

        maior(one_number,second_number, three_number)
    case 3:
        def iniciais(nome):
            palavras = nome.split()
            iniciais = ''.join([palavra[0].upper() for palavra in palavras]) 
            return iniciais
        
        nome = input("Coloque seu nome: ")
        iniciais = iniciais(nome)
        print(iniciais)
    case 4:
        def aprovado(nota1,nota2):
            media = nota1 + nota2// 2
            if media>= 60:
                return True
            return False
        
        primeira_nota = int(input("Primeira Nota: "))
        segunda_nota = int(input("Segunda Nota: "))
        aprovado = aprovado(primeira_nota,segunda_nota)
        print(aprovado)


    case 5:
        def iniciais(nome):
            palavras = nome.split()
            iniciais = ''.join([palavra[0].upper() for palavra in palavras]) 
            return iniciais
        
        nome = input("Coloque seu nome: ")
        iniciais = iniciais(nome).upper()
        print(iniciais)