#Repetição simples: 10 vezes - de 0 a 9
print("Exemplo 1")
for i in range(0, 10):
    print(i, "Vezes")


#Repetição com passo <> 1: repete 5 vezes de 2 em 2
print("Exemplo 2")
for i in range(0, 10, 2):
    print(i, "número")

#repetição decrescente
print("Exemplo 3")
for i in range(10, 0, -1):
    print(i, "Número")

#repetição com listas
print("Exemplo 4.1 - imprime o nome da lista")
alunos = ["Júlia", "Kayky", "Inessa", "Adriano"] 
for nome in alunos:
    print(nome)

print("Exemplo 4.2 - Imprime posição e nome")
for index, nome in enumerate(alunos):
    print(index, nome)
