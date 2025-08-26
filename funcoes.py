from livros import *
<<<<<<< HEAD
import os
def ListagemPorID():
    for chave, Livro in biblioteca.items():
        if Livro.getStatus() == True:
            print(f"ID: [{chave}] |  Livro Disponível  | Livro: {Livro.getTitulo()} - {Livro.getAutor()}")
        else:
            print(f"ID: [{chave}] | Livro Indisponível | Livro: {Livro.getTitulo()} - {Livro.getAutor()}")

def ListagemAutor():
    autores = {}
    for livro in biblioteca.values():
        autor = livro.getAutor()
        if autor not in autores:
            autores[autor] = []
        autores[autor].append(livro.getTitulo())
    for autor, livros in autores.items():
        print(f'{autor}:')
        for titulo in livros:
            print(f'    - {titulo}')

def ListagemGenero():
    generos = {}
    for livro in biblioteca.values():
        genero = livro.getGenero()
        if genero not in generos:
            generos[genero] = []
        generos[genero].append(livro.getTitulo())
    for genero, livros in generos.items():
        print(f'{genero}:')
        for titulo in livros:
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
        id_do_livro=float(input("Insira o ID do livro desejado:\n--> "))
        os.system("cls")
        if biblioteca[id_do_livro].getStatus() == True:
            print(f"Livro selecionado: {biblioteca[id_do_livro].getTitulo()} - {biblioteca[id_do_livro].getAutor()} | {Biblioteca[id_do_livro].getGenero()}")
            conf=input("O Livro está disponível para empréstimo. Confirmar empréstimo? (y/n)\n---> ")
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
        nome_do_livro=input("Nome do livro que você deseja devolver:\n--> ")
        os.system("cls")
        autor = input("Autor do livro que você irá devolver:\n--> ")
        os.system("cls")
        achado=False
        for livros in livros:
            if livros.nome.lower()==nome_do_livro.lower() and livros.autor.lower()==autor.lower():
                encontrado=True
                if not livros.disponivel:
                    livros.disponivel=True
                    print(f"Você devolveu o livro '{livros.nome}'. Obrigado!")
                else:
                    print(f"O livro '{livros.nome}' já está disponível na biblioteca.")
                break
        if not encontrado:
            print("Livro não encontrado. Verifique os detalhes e tente novamente.")
        input("Pressione Enter para continuar...")
        break
    continuar=input("Deseja devolver outro livro? (Sim/Não): ").strip().lower()
    if continuar!="sim":
        return
=======

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

def editar_detalhes():
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
    print("Selecione um livro para editar")

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
            editar_detalhes()
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
>>>>>>> c18b202bcd7b53efe6622a831f101c9336433f23
