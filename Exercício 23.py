# 23 - Altere o programa anterior para mostrar no final a soma dos números.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
soma = 0

if segundo_numero > primeiro_numero:
    for intervalo in range(primeiro_numero +1, segundo_numero):
        soma += intervalo
        print(intervalo)
    print(f"A soma do intervalo é: {soma}")
else:
    for intervalo in range(segundo_numero +1, primeiro_numero):
        soma += intervalo
        print(intervalo)
    print(f"A soma do intervalo é: {soma}")