preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual de desconto: '))
desconto = preco * (percentual / 100)
final = preco - desconto

print(f'O preço do produto é {preco} reais. Desconto de {percentual}%.')
      
print (f'O valor calculado de desconto: {desconto} reais. Valor final do produto: {final} reais')