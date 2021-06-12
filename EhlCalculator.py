import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Usuário insere os dados

agentes = input('Quais agentes estão sendo usados?: ')
ehl = float(input("Escreva o valor de EHL:  "))
valor_A = float(input("Escreva o primeiro valor:  "))
valor_B = float(input("Escreva o segundo valor:  "))

# Sistema faz a conta

multiplicacao1 = ehl * 100
multiplicacao2 = valor_A * 100
conversao = -valor_A
subtracao = multiplicacao1 - multiplicacao2
soma1 = conversao + valor_B
resultado = subtracao / soma1

# Apresentação ao usuário

print(f"O resultado do primeiro valor é {resultado}")

final = input('Deseja saber o resultado do segundo valor? (s/n): ')

if final.isnumeric():
    print('Ops! É permitido somente escrever "s ou n"')

elif final == 's':
    print(f'O resultado do segundo valor é: {100 - resultado}')
else:
    print('Ok, bons estudos!')
    restart_program()

questao = input('Formular resposta automaticamente? (s/n): ')

if questao == 's':
    if resultado < 100:
        print(f'É possível preparar a emulsão {agentes}, pois o valor está abaixo de 100')
        restart_program()
    elif resultado > 100:
        print(f'Não é possível preparar a emulsão {agentes}, pois o valor está acima de 100')
        restart_program()
else:
    print('Ok, bons estudos!')
    restart_program()
