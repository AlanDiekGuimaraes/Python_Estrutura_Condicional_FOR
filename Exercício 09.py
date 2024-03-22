# 09 - Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.

for numero in range (1,11):
  print(f"Tabuada do Nº {numero}")
  for contador in range(1,11):
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
