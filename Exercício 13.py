# 13 - Uma loja deseja cadastrar 5 clientes (valores) e verificar se o faturamento da loja
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse valor
# mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

soma = 0
fat_2 = 54000

for contador in range(1,6):
  fat_1 = float(input("Digite o valor do faturamento "))
  soma += fat_1
if soma > fat_2:
  print(f"O valor foi superado em R$ {soma-fat_2}")
