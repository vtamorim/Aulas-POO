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
        primeiro = input("Digite o primeiro horário no formato hh:mm ")
        segundo = input("Digite o segundo horário no formato hh:mm ")
        hora = (int(primeiro[0]) + int(primeiro[1])) + (int(segundo[0]) + int(segundo[1]))
        minuto =  int(primeiro[3]) + int(segundo[3])
        if (int(primeiro[3]) + int(segundo[3])) > 6:
            minuto = (minuto) - 6
            hora = hora + 1
        print(f"Total de Horas = 0{hora}:{minuto}0")
    case 5:
        meses = {
            1:"Janeiro",
            2:"Fevereiro",
            3:"Março",
            4:"Abril",
            5:"Maio",
            6:"Junho",
            7:"Julho",
            8:'Agosto',
            9:"Setembro",
            10:"Outubro",
            11:"Novembro",
            12:"Dezembro"
        }

        print("Informe o número do mês")
        number = int(input())
        incluido = ""

        if number <= 3:
            incluido  = "primeiro"
        elif number <= 6:
            incluido = "segundo"
        elif number <= 9:
            incluido = "terceiro"
        else:
            incluido = "quarto"

        print(f"O mês de {meses[number]} é do {incluido} trimestre")
    case 6:
        print("Digite três valores inteiros:")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())

        print(f"A soma do maior com o menor número é {min(n1,n2,n3) + max(n1,n2,n3)}")
    case 7:
        import cmath 

        def resolver_equacao_quadratica(a, b, c):
         
            discriminante = cmath.sqrt(b**2 - 4*a*c)
            if discriminante < 0:
                return "impossivel calcular"
            else:      
                raiz1 = (-b + discriminante) / (2*a)
                raiz2 = (-b - discriminante) / (2*a)
                
                return raiz1, raiz2

       
        a = 1
        b = -3
        c = 2

        raiz1, raiz2 = resolver_equacao_quadratica(a, b, c)

        print(f"As raízes são: {raiz1} e {raiz2}")
    case 8:
        print("Digite quatro valores inteiros")
        n1 = int(input())
        n2 = int(input())
        n3 = int(input())
        n4 = int(input())

        print(f"Maior valor = {max(n1,n2,n3,n4)}")
        print(f"Menor valor = {min(n1,n2,n3,n4)}")
        
        
        print(f"A soma do segundo maior valor com o segundo menor =  {max(n1,n2,n3,n4)}")

        print(min)
    case 9:
        def calcular_angulo(horas, minutos):
           
            if horas < 1 or horas > 12 or minutos < 0 or minutos > 59:
                return "Hora Inválida"

            minutos_angulo = 6 * minutos
            horas_angulo = 30 * horas + 0.5 * minutos

            angulo = abs(horas_angulo - minutos_angulo)
            menor_angulo = min(angulo, 360 - angulo)
            
            return f"O menor ângulo é {menor_angulo:.0f} graus."

        horario = input("Digite o horário no formato hh:mm ")

        horas = int(horario[0] + horario[1])
        minutos = int(horario[3] + horario[4])

        resultado = calcular_angulo(horas, minutos)
        print(resultado)
    case 10:
        data = input('Digite uma data no formato dd/mm/aaaa')
        dia = int(data[0] + data[1])
        mes = int(data[3] + data[4])
        ano = int(data[6:10])
        validaçao = ''
        if dia > 31 or 1900>ano or ano >2100 or not 1<=mes<=12:
            validaçao = "A data informada não é válida"
            print(validaçao)
        else:
            print("A data informada é válida")
    case 11:

        meses = {
            1:"Janeiro",
            2:"Fevereiro",
            3:"Março",
            4:"Abril",
            5:"Maio",
            6:"Junho",
            7:"Julho",
            8:'Agosto',
            9:"Setembro",
            10:"Outubro",
            11:"Novembro",
            12:"Dezembro"
        }
        data = input('Digite uma data no formato dd/mm/aaaa')
        dia = int(data[0] + data[1])
        mes = int(data[3] + data[4])
        ano = int(data[6:10])
        print(f"A data é {dia} de {meses[mes]} de {ano}")
    case 12:
