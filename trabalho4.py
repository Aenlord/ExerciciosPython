nome = 'Vitor'
sobrenome = 'de Souza Miguel'
nome_completo = nome + ' ' + sobrenome
lista_funcionarios = [] #lista para armazenar funcionários
id_global = 5440824 #variável com valor inicial do meu RU

#função para cadastrar funcionários
def cadastrar_funcionario(id):
    nome_funcionario = input('Qual é o seu nome? ')
    setor = input('Qual é o seu setor? ').lower()
    salario = float(input('Qual é o seu salário? '))
    
    #Cria um dicionário com os dados
    funcionario = {
        "id": id,
        "nome": nome_funcionario,
        "setor": setor,
        "salario": salario
    }
    #Adiciona uma cópia do dicionário na lista de funcionários
    lista_funcionarios.append(funcionario.copy())
    print('\nFuncionário cadastrado com sucesso!\n')

#função para consultar funcionários
def consultar_funcionarios():
    while True:
        opcao = int(input('Qual opção você deseja? (1. Consultar todos / 2. Consultar por ID / 3. Consultar por setor / 4. Retornar ao menu)\n'))
        if opcao == 1: #consultar funcionários
            if lista_funcionarios:
                for funcionario in lista_funcionarios:
                    print(funcionario)
            else:
                print('Nenhum funcionário cadastrado.')
        elif opcao == 2: #consultar por ID
            id_procurado = int(input('Digite o ID: '))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_procurado:
                    print(funcionario)
                    break
            else:
                print('Funcionário não encontrado')
        elif opcao == 3: #consultar por setor
            setor_procurado = input ('Digite o setor: ').lower()
            encontrados = []

            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_procurado:
                    encontrados.append(funcionario)
            if len(encontrados) > 0:
                for funcionario in encontrados:
                    print(funcionario)
            else:
                print('Nenhum funcionário nesse setor.')
        
        elif opcao == 4: #retorna ao menu principal
            return
        
        else:
            print('Opção inválida.')
    
#função para remover funcionários
def remover_funcionario():
    while True:
        try:
            id_remover = int(input('Qual ID você deseja remover? '))
        except ValueError:
            print('ID inválido. Digite um número.')
            continue

        for funcionario in lista_funcionarios:
            if id_remover == funcionario['id']:
                lista_funcionarios.remove(funcionario)
                print('Funcionário removido com sucesso!')
                return
        print('Id inválido. Tente novamente')
    
#Menu principal
print(f'Seja bem vindo a empresa do {nome_completo}') #mensagem de boas vindas
while True:
    main = int(input('Selecione a opção desejada: \n1.Cadastrar funcionário\n2.Consultar funcionário\n3.Remover funcionário\n4.Encerrar programa\n'))

    if main == 1:
        cadastrar_funcionario(id_global)
        id_global += 1
    elif main == 2:
        consultar_funcionarios()
    elif main == 3:
        remover_funcionario()
    elif main == 4:
        print('Encerrando o programa')
        break
    else:
        print('Opção inválida. Tente novamente')
        continue
