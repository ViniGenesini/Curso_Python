T = int(input())
for i in range(T):
    garrafas_compradas, garrafas_para_troca = map(int, input().split())
    razao = int(garrafas_compradas/garrafas_para_troca)
    if razao < 1:
        print(garrafas_compradas)
    else:
        garrafas_acumuladas = garrafas_compradas - (garrafas_para_troca*razao) + razao
        print(garrafas_acumuladas)