import os
from livros import *

# Função para limpar a tela do terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# ====================
# Funções de listagem
# ====================
def ListagemPorID():
    for chave, Livro in biblioteca.items():
        status = "Disponível" if Livro.getStatus() else "Indisponível"
        print(f"ID: [{chave}] | Livro {status} | {Livro.getNome()} - {Livro.getAutor()}")


def ListagemAutor():
    autores = {}
    for Livro in biblioteca.values():
        autor = Livro.getAutor()
        if autor not in autores:
            autores[autor] = []
        autores[autor].append(Livro.getNome())
    for autor, Livros in autores.items():
        print(f'{autor}:')
        for nome in Livros:
            print(f'    - {nome}')


def ListagemGenero():
    generos = {}
    for Livro in biblioteca.values():
        genero = Livro.getGenero()
        if genero not in generos:
            generos[genero] = []
        generos[genero].append(Livro.getNome())
    for genero, Livros in generos.items():
        print(f'{genero}:')
        for nome in Livros:
            print(f'    - {nome}')


def ListagemDisponiveis():
    print('Livros disponíveis:')
    for chave, Livro in biblioteca.items():
        if Livro.getStatus():
            print(f"ID: [{chave}] || Livro: {Livro.getNome()} - {Livro.getAutor()}")


def ListagemEmprestados():
    print('Livros emprestados:')
    for chave, Livro in biblioteca.items():
        if not Livro.getStatus():
            print(f"ID: [{chave}] || Livro: {Livro.getNome()} - {Livro.getAutor()}")


# ====================
# Funções de empréstimo e devolução
# ====================
def emprestimos():
    while True:
        limpar_tela()
        ListagemPorID()
        try:
            id_do_livro = int(input("Insira o ID do livro desejado:\n--> "))
        except ValueError:
            print("ID inválido!")
            os.system("pause")
            break
        limpar_tela()
        if biblioteca[id_do_livro].getStatus():
            print(f"Livro selecionado: {biblioteca[id_do_livro].getNome()} - {biblioteca[id_do_livro].getAutor()} | {biblioteca[id_do_livro].getGenero()}")
            conf = input("O livro está disponível para empréstimo. Confirmar empréstimo? (s/n)\n---> ")
            if conf.lower() == 's':
                biblioteca[id_do_livro].setStatus(False)
                print(f"Você emprestou o livro '{biblioteca[id_do_livro].getNome()}'. Aproveite a leitura!")
                os.system('pause')
            else:
                print("Operação cancelada.")
                os.system('pause')
        else:
            print("Livro indisponível para empréstimo.")
            input("Pressione Enter para continuar...")
        break


def devolucao():
    while True:
        limpar_tela()
        print("=== Devolução de Livros ===")
        ListagemEmprestados()
        try:
            id_do_livro = int(input("Insira o ID do livro que você deseja devolver:\n--> "))
        except ValueError:
            print("ID inválido!")
            os.system("pause")
            break
        limpar_tela()
        if id_do_livro in biblioteca and not biblioteca[id_do_livro].getStatus():
            print(f"Livro selecionado: {biblioteca[id_do_livro].getNome()} - {biblioteca[id_do_livro].getAutor()}")
            conf = input("Confirmar devolução? (s/n)\n---> ")
            if conf.lower() == 's':
                biblioteca[id_do_livro].setStatus(True)
                print(f"Você devolveu o livro '{biblioteca[id_do_livro].getNome()}'. Obrigado!")
                os.system('pause')
            else:
                print("Operação cancelada.")
                os.system('pause')
        else:
            print("ID inválido ou livro já disponível.")
            os.system('pause')

        continuar = input("Deseja devolver outro livro? (s/n): ").strip().lower()
        if continuar != "s":
            break


# ====================
# Função de menu principal
# ====================
def menu():
    while True:
        limpar_tela()
        print("="*40)
        print("         SISTEMA BIBLIOTECA  ")
        print("="*40)
        print("1 - Listar todos os livros")
        print("2 - Listar livros por autor")
        print("3 - Listar livros por gênero")
        print("4 - Listar livros disponíveis")
        print("5 - Realizar empréstimo")
        print("6 - Realizar devolução")
        print("0 - Sair")
        print("="*40)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            ListagemPorID()
            os.system('pause')
        elif opcao == "2":
            limpar_tela()
            ListagemAutor()
            os.system('pause')
        elif opcao == "3":
            limpar_tela()
            ListagemGenero()
            os.system('pause')
        elif opcao == "4":
            limpar_tela()
            ListagemDisponiveis()
            os.system('pause')
        elif opcao == "5":
            emprestimos()
        elif opcao == "6":
            devolucao()
        elif opcao == "0":
            print("Saindo do sistema... até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            os.system('pause')
