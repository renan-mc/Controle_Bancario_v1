'''
Desafio de controle bancário

--- TODO ---
O app deve conter operação de saque, depósito e extrato
O limite máximo por saque deve ser de R$ 500,00
O número máximo de saques por dia é 3
Não tem limite de depósitos
O extrato deve conter todas as movimentações do dia além do saldo atual
Não podem ser inseridos valores negativos!

'''

import os
clear = lambda: os.system('clear')

saldo_inicial = 100.00
saldo = saldo_inicial
LIMITE_DE_SAQUES = 3
limite_por_saque = 500.00
numero_de_saques_realizados = 0
movimentacoes_realizadas = ''


menu = '''



Aplicativo de controle bancário.

Digite a operação desejada:

[1] Extrato
[2] Saque
[3] Depósito
[0] Sair

'''

while True:

    operacao = int(input(menu))

    if operacao == 0:
        clear()
        print('\n\nOperação selecionada: Sair \n\nFechando o app...\n')
        break

    elif operacao == 1: #Extrato
        clear()
        print('\n\nOperação selecionada: Extrato')
        print(f'\nSaldo Inicial: R$ {saldo_inicial:.2f} \n\nMovimentações realizadas: (da mais antiga até mais recente)\n{movimentacoes_realizadas} \nSaldo Atual: R$ {saldo:.2f} \n\nRetornando ao menu...')

    elif operacao == 2: #Saque
        clear()
        print('\n\nOperação selecionada: Saque')
        if numero_de_saques_realizados < 3:
            valor_sacado = float(input('\nInsira o valor que deseja sacar (Formato R$ XXX,XX): '))
            if 0 < valor_sacado <= 500.00:
                if valor_sacado < saldo:
                    saldo -= valor_sacado
                    numero_de_saques_realizados += 1
                    print(f'\nOperação realizada! \nValor sacado: R$ {valor_sacado:.2f} \nSaldo após saque: R$ {saldo:.2f} \nSaques realizados hoje: {numero_de_saques_realizados} (Limite de {LIMITE_DE_SAQUES} saques por dia) \n\nRetornando ao menu...')
                    movimentacoes_realizadas += f'\nSaque realizado no valor de R$ {valor_sacado:.2f}'
                else:
                    print(f'\nVocê não possui esta quantia em conta atualmente. Saldo atual: R$ {saldo:.2f} \n\nRetornando ao menu...')
            else:
                print(f'\nNão é possível sacar valores negativos ou maiores do que R$ {limite_por_saque:.2f}! \n\nRetornando ao menu...')
        else:
            print(f'\nLimite máximo de saques por dia alcançado ({LIMITE_DE_SAQUES} saques) \n\nRetornando ao menu...')

    elif operacao == 3: #Depósito
        clear()
        print('\n\nOperação selecionada: Depósito')
        valor_depositado = float(input('\nInsira o valor que deseja depositar (Formato R$ XXX,XX): '))
        if valor_depositado > 0:
            saldo += valor_depositado
            print(f'\nOperação realizada! \nValor depositado: R$ {valor_depositado:.2f} \nSaldo após depósito: R$ {saldo:.2f} \n\nRetornando ao menu...')
            movimentacoes_realizadas += f'\nDepósito realizado no valor de R$ {valor_depositado:.2f}'
        else:
            print('\nNão é possível depositar valores negativos! Retornando ao menu...')

    else:
        clear()
        print('\n\nOpção não encontrada... por favor tente novamente.')