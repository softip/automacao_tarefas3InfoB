from funcoes import login

while True:
    user = input('Digite o nome do usuário:')
    pwd = input('Digite a senha do usuário:')
    if login(user, pwd):
        print('Logado com sucesso')
        break
    else:
        print('Tente novamente!')