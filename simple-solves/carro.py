dias = int(input("Quantos dias o carro foi alugado?"))
kms = float(input("Quantos Km foram percorridos?"))
calcDias = (60 * dias) +  (0.15 * kms)
print(f"O valor a pagar é: {calcDias:.1f}R$")