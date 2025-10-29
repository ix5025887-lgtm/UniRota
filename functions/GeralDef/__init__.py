from functions import screen
from time import sleep
import csv

def PasswordReset(email):
    from random import randint
    logins = open("logins.txt")
    linhas = logins.read().splitlines()
    logins.close()

    if email in linhas:
        codigo_reset = f"{randint(0, 999):03}"

        reset = open("codigo.txt", "w")
        reset.write(codigo_reset + "\n")
        reset.close()

        reset = open("codigo.txt", "r")
        codigoreset = reset.read().splitlines()
        reset.close()
        
        print("Se esse email estiver cadastrado, ensira o código que foi enviado")
        codigo = input("Digite o código de reset: ")

        if codigo == codigoreset[0]:
            posicao_senha = linhas.index(email)+1
            linhas[posicao_senha] = input("Digite a nova senha: ")
            logins = open("logins.txt", "w")
            logins.writelines([linha + "\n" for linha in linhas])
            logins.close()
            print("Senha alterada com sucesso!")
        else:
            print("Código incorreto!")
    else:
        print("Se esse email estiver cadastrado, ensira o código que foi enviado")
        codigo = input("Digite o código de reset: ")
        print("Código incorreto!")


def CreateNotice():
    from datetime import datetime
    while True:
        print("Digite o Aviso [SAIR para encerrar]:")
        text = str(input("-> "))
        if text.upper() == 'SAIR':
            break
        date = datetime.now()
        date_time = date.strftime("%d/%m/%Y %H:%M:%S")
        novo_aviso = f"[{date_time}] {text}\n"

        arquivo = open("avisos.txt", "r", encoding="utf-8")
        conteudo_antigo = arquivo.read()
        arquivo.close()

        avisos = open("avisos.txt", "w", encoding="utf-8")
        avisos.write(novo_aviso + conteudo_antigo)
        avisos.close()

        print("Aviso salvo com sucesso")

def caminho_adm(linhas, posicao_tipo):
    if linhas[posicao_tipo] == "administrador":
        screen.menu_adm(linhas[posicao_tipo])
        opc = int(input("opc = "))
        screen.clear()

        if opc == 1:

            with open("lista_de_alunos.txt", "r") as arquivo:
                alunos=arquivo.read().splitlines()

                lista={}

                for pessoa in alunos:
                    if ";" not in pessoa:
                        continue

                    aluno = pessoa.split(";")[0]
                    faculdade = pessoa.split(";")[1]
                    lista[aluno.strip()] = faculdade.strip()

                for aluno, faculdade in lista.items():
                    print(f"{aluno} — {faculdade}")
                while True:
                    opc=int(input('''
[1]: Exportar para CSV
[2]: Sair                      
'''))
                    if opc==1:
                        screen.clear()
                        print("Exportando...")
                        sleep(0.2)
                        with open("alunos_exportados.csv", "w", newline="", encoding="cp1252") as csvfile:
                            writer = csv.writer(csvfile, delimiter=";")
                            writer.writerow(["Aluno", "Faculdade"])
                            for aluno, faculdade in lista.items():
                                writer.writerow([aluno, faculdade])
                        print("Exportado com sucesso para 'alunos_exportados.csv'!\n")
                        sleep(1)
                        
                    elif opc == 2:
                        print("Saindo...")
                        sleep(0.5)
                        break

                    else:
                        print("Opção inválida! Tente novamente.")
