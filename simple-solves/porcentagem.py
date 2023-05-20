valor = float(input('Digite o valor: R$'))
desconto = float(input('Digite a porcentagem de desconto:'))
result = valor*desconto/100
print(f"O valor: R${valor}, com desconto de: {desconto}%, Resulta em: R${valor-result:.2f}")