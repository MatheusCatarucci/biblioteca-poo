from livros import *
import os

def ListagemPorID():
    for chave, Livro in biblioteca.items():
        if Livro.getStatus() == True:
            print(f"ID: [{chave}] |  Livro Disponível  | Livro: {Livro.getTitulo()} - {Livro.getAutor()}")
        else:
            print(f"ID: [{chave}] | Livro Indisponível | Livro: {Livro.getTitulo()} - {Livro.getAutor()}")

def ListagemAutor():
    autores = {}
    for Livro in biblioteca.values():
        autor = Livro.getAutor()
        if autor not in autores:
            autores[autor] = []
        autores[autor].append(Livro.getTitulo())
    for autor, Livros in autores.items():
        print(f'{autor}:')
        for titulo in Livros:
            print(f'    - {titulo}')

def ListagemGenero():
    generos = {}
    for Livro in biblioteca.values():
        genero = Livro.getGenero()
        if genero not in generos:
            generos[genero] = []
        generos[genero].append(Livro.getTitulo())
    for genero, Livros in generos.items():
        print(f'{genero}:')
        for titulo in Livros:
            print(f'    - {titulo}')

def ListagemDisponiveis():
    print('Livros disponíveis:')
    for chave, Livro in biblioteca.items():
        if Livro.getStatus() == True:
            print(f"ID: [{chave}] || Livro: {Livro.getTitulo()} - {Livro.getAutor()}")

def emprestimos():
    while True:
        os.system("cls")
        print(" _________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |_________|")
        print("")
        os.system("cls")
        ListagemPorID()
        id_do_livro = int(input("Insira o ID do livro desejado:\n--> "))
        os.system("cls")
        if biblioteca[id_do_livro].getStatus() == True:
            print(f"Livro selecionado: {biblioteca[id_do_livro].getTitulo()} - {biblioteca[id_do_livro].getAutor()} | {biblioteca[id_do_livro].getGenero()}")
            conf = input("O Livro está disponível para empréstimo. Confirmar empréstimo? (y/n)\n---> ")
            if conf.lower() == 'y':
                biblioteca[id_do_livro].setStatus(False)
                print(f"Você emprestou o livro ''{biblioteca[id_do_livro].getTitulo()}''. Aproveite a leitura!")
                os.system('pause')
            elif conf.lower() == 'n':
                print("Saindo...")
                os.system('pause')
                break
            else:
                print("Nenhuma opção válida selecionada, saindo...")
                os.system('pause')
                break
        else:
            print("Livro indisponível para empréstimo.")
            input("Pressione Enter para continuar...")
            break
        break
    
def devolucao():
    while True:
        os.system("cls")
        print(" ____________________________\n |                          |\n |                          |\n |     Devolução dos Livros |\n |                          |\n |__________________________|")
        nome_do_livro = input("Nome do livro que você deseja devolver:\n--> ")
        os.system("cls")
        autor = input("Autor do livro que você irá devolver:\n--> ")
        os.system("cls")
        achado = False
        for Livro in biblioteca.values():
            if Livro.getTitulo().lower() == nome_do_livro.lower() and Livro.getAutor().lower() == autor.lower():
                achado = True
                if not Livro.getStatus():
                    Livro.setStatus(True)
                    print(f"Você devolveu o livro '{Livro.getTitulo()}'. Obrigado!")
                else:
                    print(f"O livro '{Livro.getTitulo()}' já está disponível na biblioteca.")
                break
        if not achado:
            print("Livro não encontrado. Verifique os detalhes e tente novamente.")
        input("Pressione Enter para continuar...")
        break

    continuar = input("Deseja devolver outro livro? (Sim/Não): ").strip().lower()
    if continuar != "sim":
        return

