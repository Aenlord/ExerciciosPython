nome = 'Vitor'
sobrenome = 'Miguel'
nome_completo = nome + ' ' + sobrenome
print(f'Bem vindo a loja do {nome_completo}!')
valorDoPedido = float(input('Qual o valor do seu seu pedido? '))
quantidadedeParcelas = int(input('Deseja parcelar em quantas vezes? '))

if quantidadedeParcelas < 4:
    juros = 0

elif quantidadedeParcelas >= 4 and quantidadedeParcelas < 6:
    juros = 4/100

elif quantidadedeParcelas >= 6 and quantidadedeParcelas < 9:
    juros = 8/100

elif quantidadedeParcelas >= 9 and quantidadedeParcelas < 13:
    juros = 16/100

else:
    juros = 32/100

valorDaParcela = valorDoPedido * (1 + juros) / quantidadedeParcelas
valorTotalParcelado = valorDaParcela * quantidadedeParcelas

print(f'O valor das parcelas é de R${valorDaParcela}')
print(f'O valor total parcelado é de R${valorTotalParcelado}')
