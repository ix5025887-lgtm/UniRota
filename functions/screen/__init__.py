

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('''
Bem vindo ao Unirota!

[1]: Fazer Login
[2]: Redefinir Senha
[3]: Sair''')
    
def menu_adm(x):
        print(f'''
Menu {x}

[1]: Lista de alunos
[2]: Editar universidades
[3]: Editar Alunos
[4]: Acompanhar rota
[5]: Adicionar aviso
[5]: Minha conta
[7]: Sair
''')
