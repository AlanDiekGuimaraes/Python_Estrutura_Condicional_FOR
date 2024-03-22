# 19 - Faça um programa que peça dois números, base e expoente, calcule e mostre
# o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite o valor base: "))
expoente = int(input("Digite o expoente: "))
result = 1
for i in range(expoente):
    if base == 1:
        result = base
    else:
        result *= base
    print(f"Resultado {result}")
