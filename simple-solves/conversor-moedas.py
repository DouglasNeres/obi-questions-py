print("1- REAL")
print("2- DÓLAR")
moeda = input("Qual moeda você deseja converter?")
if(moeda == '1'):
  var = float(input("Digite seu Valor em Real R$:"))
  print(f"O valor em Dólar é: US${var/5}")
elif(moeda == '2'):
  var = float(input("Digite seu Valor em Dólar US$:"))
  print(f"O valor em reais é: R${var*5}")
else:
  print("Nenhum valor reconhecido!")
