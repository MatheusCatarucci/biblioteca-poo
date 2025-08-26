import os
from livros import *

def limpar_tela():
    os.system("cls")

def ListagemPorID():
    for chave, Livro in biblioteca.items():
        print(50 * "-")
        print(f"ID: {chave}".center(50))
        print(50 * "-")
        print(f"Título: {Livro.getNome()}")
        print(f"Autor: {Livro.getAutor()}")
        print(f"Gênero: {Livro.getGenero()}")
        if Livro.getStatus():
            print("Livro disponível para troca")
        else:
            print("Livro indisponível para troca")
    print(50 * "-")
    os.system("pause")

def add_livro():
        global status

        limpar_tela()
        print("==== ADICIONAR LIVRO ====\n")
        nome_livro = input("Digite o título do livro\n--> ")
        autor_livro = input("Digite o autor do livro\n--> ")
        genero = input("Digite o gênero do livro\n--> ")
        status = input("O livro está disponível para troca? (s/n)\n--> ")
        
        if status == "s":
            limpar_tela()
            status = True
            pass
        elif status == "n":
            limpar_tela()
            status = False
            pass
        else:
            limpar_tela()
            print("Digite uma opção válida")
        
        biblioteca[len(biblioteca)+1] = Livro(nome=nome_livro, autor=autor_livro, genero=genero, status=status)

def listagem():
    limpar_tela()
    print("==== LISTAR LIVROS ====\n")
    print("1 - Listar Livros")
    print("0 - Sair")
    escolha = int(input("Escolha uma opção\n--> "))
    if escolha == 1:
        limpar_tela()
        ListagemPorID()
    elif escolha == 0:
        limpar_tela()
        os.system("cls")
        exit()
    else:
        limpar_tela()
        print("Escolha inválida")
        os.system("pause")

def menu():
    while True:
        limpar_tela()
        print("==== BIBLIOTECA ====\n")
        print("1 - Adicionar livro")
        print("2 - Remover livro")
        print("3 - Listar todos os livros")
        print("4 - Listar livro autor")
        print("5 - Editar detalhes")
        print("6 - Emprestar livro")
        print("7 - Devolver livro")
        print("Escolha uma opção acima")
        escolha = int(input("--> "))

        if escolha == 1:
            add_livro()
        elif escolha == 2:
            pass
        elif escolha == 3:
            listagem()
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass
        elif escolha == 6:
            pass
        elif escolha == 7:
            pass
        elif escolha == 0:
            os.system("pause")
            exit()
        else:
            print("Escolha uma opção válida")
            os.system("pause")
