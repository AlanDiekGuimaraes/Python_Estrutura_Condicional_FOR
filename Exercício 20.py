# 20 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# numero = int(input("Informe um número para mostrarmos os números primos entre 1 e o valor digitado"))


n = int(input("Digite um número: "))
for numeroTestado in range(1, n+1):
    for numeroDivisor in range(numeroTestado):
        print(f"{numeroTestado} / {numeroDivisor+1} = {numeroTestado /(numeroDivisor+1)} com o resto {numeroTestado%(numeroDivisor+1)}")
        if numeroTestado % (numeroDivisor+1) == 0:
            if 1 != numeroDivisor+1 != numeroTestado:
                print("não é primo\n")
                break
            elif numeroDivisor+1 == numeroTestado:
                print("número é primo\n")