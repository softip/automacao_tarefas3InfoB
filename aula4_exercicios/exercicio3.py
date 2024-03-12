'''
Exercício 3
-------------------------------------------------------------
Crie um programa que execute repetidamente o programa do 
exercício 2. Após a apresentação do resultado o programa deve 
perguntar se o usuário deseja continuar a calcular, se a resposta
for S (Sim) o programa deve continuar se a resposta for N (Não) 
o programa deve terminar.
'''


while True:
    desejo = input("Deseja continuar? [S/N]")
    if desejo == "N":
        break
    else:
        #Entradas
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite um número: "))
        op = input("Digite operador matemático: ")

        #processamento
        if op == '+':
            resultado = n1 + n2
            print('O resultado da soma é ', resultado)
        elif op == '-':
            resultado = n1 - n2
            print('O resultado da subtração é ', resultado)
        elif op == '/':
            resultado = n1 / n2
            print('O resultado da divisão é ', resultado)
        elif op == '*':
            resultado = n1 * n2
            print('O resultado da multiplicação é ', resultado)
        else:
            print('Operador desconhecido')

