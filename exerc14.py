def borda (s1):
    tam = len(s1)
    if tam:
        print('+','-' * tam, '+')
        print('|',s1,'|')
        print('+','-' * tam, '+')

borda('Olá mundo!')

borda('Botafogo de futebol e Regatas')