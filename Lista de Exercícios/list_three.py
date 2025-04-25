numero  = int(input("Número da Questão: "))
import math
match numero:
    case 1:
        primeiro = int(input())
        segundo = int(input())
        PROD = primeiro * segundo
        print(f"PROD = {PROD}")
    case 2:
        primeiro = float(input())
        segundo = float(input())
        media = (primeiro * 3.5 + segundo * 7.5) / 11
        print(f"MEDIA = {media:.5f}")
    case 3:
        pi = 3.14159
        raio = float(input())
        volume = (4.0 / 3) * pi * (raio ** 3)
        print(f"VOLUME = {volume:.3f}")
    case 4:
        C, N = map(int, input().split())
        termino = C % N
        print(termino)

    case 5:
        import math
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(f"{distancia:.4f}")

    case 6:
        T1, T2, T3, T4 = map(int, input().split())
        total = T1 + T2 + T3 + T4 - 3
        print(total)