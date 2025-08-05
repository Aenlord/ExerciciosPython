palavras = ('arroz', 'feijão', 'tomate', 'amora', 'banana', 'melão', 'melancia', 'limão', 'laranja', 'morango')

for alimento in palavras:
    print(f'\nPalavra: {alimento.upper()}. Vogais: ')
    for letra in alimento:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
