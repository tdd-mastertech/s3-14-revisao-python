# print: comando para imprimir em tela um texto
# \n: uma quebra de linha
print('Bem-vindx ao banco XPTO')
print('Para seu cadastro, preencha as seguintes informações\n')

# criação de variável nome
# input: entrada de dados
nome = input('Digite seu nome: ')

# por padrão a entrada do input é texto, para convertermos em um número inteiro,
# é necessário colocar o int na frente
idade = int(input('Digite sua idade: '))

if idade > 16:

    # simulação de saldo
    saldo = 2300.50

    # Ações da variável de entrada para atm
    print('\nDigite 1 para depósito')
    print('Digite 2 para saque')
    print('Digite 3 para empréstimo\n')

    entrada_atm = int(input('Digite a ação desejada: '))
    
    # if: condição
    # elif: outras condições que fazem parte do mesmo bloco lógico
    # else: caso contrário

    # == : igual
    # > : maior
    # < : menor
    # >= : maior ou igual
    # <= : menor ou igual
    # != : diferente
    
    # se a variável de entrada_atm for igual a 1, a opção de escolha será de depósito

    if entrada_atm == 1:
        print(f'Olá {nome}, você digitou a opção de depósito\n')
        valor_deposito = float(input('Digite o valor de depósito: '))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            print(f'{nome}, seu saldo é de: R${saldo}')
        else:
            print('O valor não pode ser negativo.')

    elif entrada_atm == 2:
        print(f'Olá {nome} você digitou a opção de saque\n')
        valor_saque = float(input('Digite o valor de saque: '))
        if valor_saque < 1000:
            saldo = saldo - valor_saque
            print(f'{nome}, seu saldo é de: R${saldo}')
        else:
            print('O valor de saque não pode ser maior do que R$ 1000.00')
    
    elif entrada_atm == 3:
        print(f'Olá {nome}, você digitou a opção de empréstimo\n')
        valor_emprestimo = float(input('Digite o valor de empréstimo: '))
        salario = float(input('Digite o valor de seu salário: '))

        if(valor_emprestimo > (10*salario)):
            print(f'O seu empréstimo foi recusado.')
        else:
            print(f'O seu empréstimo foi aceito')
            saldo = valor_emprestimo + saldo
            print(f'{nome}, seu novo saldo é de: R${saldo}')
else:
    print(f'{nome}, não podemos finalizar seu cadastro.')

# o 'f' dentro do print é para conseguirmos unir uma variável com um texto,
# assim realizamos a concatenação

print('\n\n\n*********Fim de operação***********')