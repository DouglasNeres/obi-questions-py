name = input("Digite seu nome Completo:").strip()

print("Analisando seu nome...")
print(f"Seu nome em Maiúsculas é: {name.upper()}")
print(f"Seu nome em Minúsculas é: {name.lower()}")
print(f"Seu nome tem ao todo: {len(name)-name.count(' ')} letras")
# print(f"Seu primeiro nome é: {name.find(' ')}")
separa = name.split()
print(separa)