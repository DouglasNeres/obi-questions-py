salario = float(input("Digite o seu salário: R$"))
porcentagemDeAumento = float(input("Digite o seu Aumento:"))
aumento = salario*porcentagemDeAumento/100

print(f'Seu salário com 15% de aumento é: {salario+aumento:.2f}')