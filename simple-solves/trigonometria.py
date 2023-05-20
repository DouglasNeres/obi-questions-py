co = float(input("Comprimento do Cateto Oposto:"))
ca = float(input("Comprimento do Cateto Adjacente:"))
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"Hipotenusa é: {hi:.2f}")

sin = co/hi
cos = ca/hi
tan = co/ca

print(f"E seu Seno é: {sin}, Cossseno é: {cos} e a tangente é: {tan}")
