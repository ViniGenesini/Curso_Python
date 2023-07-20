N = int(input())
n = N
while n > 0:
    contador = 0
    total_caracteres_a = 0
    total_caracteres_b = 0
    A, B = (input().split())
    for caracter in A:
        total_caracteres_a += 1
    for caracter in B:
        total_caracteres_b += 1
    if total_caracteres_a <= 1000 or total_caracteres_b <= 1000:
        if total_caracteres_b > total_caracteres_a:
            print("nao encaixa")
            n -= 1
        else:
            indice = total_caracteres_b
            while indice > 0:
                if A[-indice] == B[-indice]:
                    contador += 1
                indice -= 1
            if total_caracteres_b == contador:
                print("encaixa")
            else:
                print("nao encaixa")
            n -= 1
