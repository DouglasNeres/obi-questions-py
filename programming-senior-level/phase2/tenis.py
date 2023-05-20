def menor_diferenca_das_duplas(niveis):
    menor_diferenca = float('inf')  
    for i in range(len(niveis) - 1):
        for j in range(i + 1, len(niveis)):
            time1 = niveis[i] + niveis[j]
            time2 = sum(niveis) - time1
            diferenca = abs(time1 - time2) 
            
            if diferenca < menor_diferenca:
                menor_diferenca = diferenca

    return menor_diferenca

niveis = []
for _ in range(4):
    nivel = int(input())
    niveis.append(nivel)

resultado = menor_diferenca_das_duplas(niveis)

print(resultado)