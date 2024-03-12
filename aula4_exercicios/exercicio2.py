'''
Exercício 2
--------------------------------------------------------
Crie um programa que recebe 2 números reais como entrada e um 
operador matemático. De acordo com o operador matemático fornecido
o programa deve calcular e apresentar o resultado da operação.
Exemplo de Entrada
1.2 
2.3 
+

Exemplo Saída
O resultado da soma é 3.5
'''

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




