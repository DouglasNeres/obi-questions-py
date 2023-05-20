from random import choice

n1 = input("1°:")
n2 = input("2°:")
n3 = input("3°:")
n4 = input("4°:")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f"O escolhido foi: {escolhido}")