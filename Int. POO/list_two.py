import math

question = int(input("Número da Questão: "))

match question:
    case 1:
        class Retangulo:
            def __init__(self):
                self.__b = 0
                self.__h = 0
            def SetBase(self,base):
                if base <= 0 or isinstance(base,(str)): raise ValueError("Insira um valor inválido")
                self.__b = base
            def SetAltura(self,altura):
                if altura <= 0 or isinstance(altura,(str)): raise ValueError("Insira um valor inválido")
                self.__h = altura
            def GetBase(self):
                return self.__b
            def GetAltura(self):
                return self.__h
            def CalcArea(self):
                return self.__h * self.__b
            def CalcDiagonal(self):
                return math.sqrt(self.__h**2 + self.__b**2)
            def ToString(self):
                return f"Base do Retângulo: {self.__b}\nAltura do Retângulo: {self.__h}"

        rectang = Retangulo()
        altura = int(input("H: "))
        base = int(input("B: "))
        rectang.SetAltura(altura)
        rectang.SetBase(base)
        print("[0] Base\n[1] Altura\n[2] Calcular Área\n[3] Calcular Diagonal\n[4]Atributos ")
        escolha = input()
        match escolha:
            case "0"|"Base":
                print(rectang.GetBase())
            case "1"|"Altura":
                print(rectang.GetAltura())
            case "2"|"Calcular Área":
                print(rectang.CalcArea())
            case "3"|"Calcular Diagonal":
                print(rectang.CalcDiagonal())
            case "4"|"Atributos":
                print(rectang.ToString())
    case 2:
        class Frete:
            def __init__(self):
                self.__d = 0
                self.__p = 0
            def SetDistancia(self,distancia):
                if distancia<=0: raise ValueError("Insira um número válido")
                self.__d = distancia
            def SetPeso(self,peso):
                if peso<=0: raise ValueError("Insira um número válido")
                self.__p = peso
            def GetDistancia(self):
                return self.__d
            def GetPeso(self):
                return self.__p
            def CalcFrete(self):
                return self.__d * 0.01
            def ToString(self):
                return f"Distancia: {self.__d}km\nPeso: {self.__p}kg"
        ob_frete = Frete()
        distancia = int(input("D: "))
        peso = int(input("P: "))
        ob_frete.SetDistancia(distancia)
        ob_frete.SetPeso(peso)
        print("[0] Distancia\n[1] Peso\n[2] Calcular Frete\n[3] Atributos")
        escolha = input()
        match escolha:
            case "0"|"Base":
                print(ob_frete.GetDistancia())
            case "1"|"Altura":
                print(ob_frete.GetPeso())
            case "2"|"Calcular Frete":
                print(ob_frete.CalcFrete())
            case "3"|"Atributos":
                print(ob_frete.ToString())
    case 3:
        class EquacaoSG:
            def __init__(self):
                self.__a = 0
                self.__b = 0
                self.__c = 0
                self.__delta = 0
            def SetA(self,a):
                if a == 0: raise ValueError("Valor inválido")
                self.__a = a
            def SetB(self,b):
                self.__b = b
            def SetC(self,c):
                self.__c = c
            def GetA(self):
                return self.__a
            def GetB(self):
                return self.__b
            def GetC(self):
                return self.__c
            def Delta(self):
                self.__delta = (self.__b**2) - (4 * self.__a * self.__c)
                return self.__delta
            def TemRaizesReais(self):
                if self.__delta <0: return False
                return True
            def Raiz1(self):
                return (-self.__b + math.sqrt(self.__delta)) / (2 * self.__a)
            def Raiz2(self):
                return (-self.__b - math.sqrt(self.__delta)) / (2 * self.__a)
            def ToString(self):
                return f"A: {self.__a}\nB: {self.__b}\nC: {self.__c}\n Delta: {self.__delta}"

        seg_grau = EquacaoSG()
        a = int(input("A: "))
        b = int(input("B: "))
        c = int(input("C: "))
        seg_grau.SetA(a)
        seg_grau.SetB(b)
        seg_grau.SetB(c)
        print("Recomendo fazer por ordem :)")
        print("[0] A\n[1] B\n[2] C\n[3] Delta\n[4] Primeira Raiz\n[5] Segunda Raiz\n[6] Atributos")
        escolha = input()
        match escolha:
            case "0"|"A":
                print(seg_grau.GetA())
            case "1"|"B":
                print(seg_grau.GetB())
            case "2"|"C":
                print(seg_grau.GetC())
            case "3"|"Delta":
                print(seg_grau.Delta())
            case "4"|"Primeira Raiz":
                print(seg_grau.Raiz1())
            case "5"|"Segunda Raiz":
                print(seg_grau.Raiz2())
            case "6"|"Atributos":
                print(seg_grau.ToString())

