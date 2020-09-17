import sqlite3
import datetime
from time import sleep
from os import system


conn = sqlite3.connect(r'banco.db')

c = conn.cursor()
system("title Banco de Namorada")

def creatTable():
    c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, idade real, nome text, endereco text, classe text)')



creatTable()





def quebra():
    print('\n')




def ano(s):
    atual = datetime.date.today().year
    return atual - s


def inserirDados():
    nome = str(input("Digite o Nome Completo: "))
    turma = str(input("Digite a Turma: "))
    enderco = str(input("Digite o Endereco: "))
    idade = int(input("Digite ano de nascimento: "))
    n = int(input("Numero: "))
    c.execute("INSERT INTO dados VALUES({} , {}, '{}', '{}', '{}')".format(n, ano(idade), nome, enderco, turma))


    conn.commit()



sql = 'SELECT * FROM dados WHERE nome = ?'


def lindo(n):
    p = len(n)
    print('\033[32m_' * p)
    print(f'\033[31m{n.upper()}\033[32m')
    print('_' * p)



while True:
    lindo('Namorada')
    print(
        "\033[32m         Menu        \n1- Inserir dados no Banco\n2- Procurar no banco\n3- informação\n4- Sair...")
    print('_' * 20)
    try:
        op = int(input('\033[31mR: '))
    except:
        lindo('Escolha uma opção valida!!')
    else:
        if op == 1:
            try:
                lindo("Dados")
                inserirDados()
            except:
                lindo('erro: não foi possivvel adicionar os dados')
            else:

                sleep(2)
                lindo("\nAdcionado com Sucesso!")
                sleep(3)



        elif op == 2:
            pesquisa = input("Pesquisa: ")
            senha = "0001"
            vez = 3
            while vez != 0:
                S = str(input(f"\n\nDigite a Senha tens {vez} tentativas: "))
                vez = vez - 1
                if S == senha:

                    try:
                        def lerDados(busca):
                            for row in c.execute(sql, (busca,)):
                                sleep(2)
                                print(row[:3])

                                sleep(5)
                

                    except:
                        lindo("Não existe no banco")
                        sleep(5)
                        break
                    else:
                        lindo("Terminando a Pesquisa")
                        sleep(2)
                        lerDados(pesquisa)
                        quebra()
                        break

                elif vez == 0:
                    lindo("Senha Incorreta")
                    sleep(5)

        elif op == 3:

            lindo('\n     informação      ')
            print(
                '\033[36m1ª opção insere dados no banco.\nAdiciona conteudos ao banco.\nBy: Naidon Marques\n')
            print(
                '2º opção é um Scan\nPesquisa e scaneia os dados pessoais no que estão no banco de dados.\nby: Naidon Marques')
            print(
                '\033[36m4- Sair \n termina o programa.\nBy: Naidon Marques\n')
            print('\033[32m_' * 20)
            sleep(3)
        elif op == 4:
            lindo('Fim')
            break

        else:
            lindo('Escolha uma opção valida!!')
        system("cls")
