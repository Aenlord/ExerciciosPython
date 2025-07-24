#Este programa solicita ao usuário que informe o preço de um produto e o percentual de desconto desejado. Com base nesses dados, ele calcula o valor do desconto e o preço final do produto após o abatimento. 
#Em seguida, exibe todas as informações na tela de forma detalhada, incluindo o preço original, o percentual de desconto, o valor do desconto e o valor final a ser pago.

preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto: '))
desconto = preco * (percentual / 100)
final = preco - desconto

print(f'O preço do produto é {preco} reais. Desconto de {percentual}%.')
      
print (f'O valor calculado de desconto: {desconto} reais. Valor final do produto: {final} reais')
