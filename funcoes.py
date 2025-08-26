import os
from livros import *
def emprestimo(biblioteca):
    while True:
        os.system("cls")
        print(" ____________________________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |__________________________|")
        print("")
        genero = int(input("Gêneros Disponiveis:\nNª1 - Ficção Literaria\nNº2 - Fantasia\nNº3 - Mistério / Suspense\nNº4 - Romance\nNº5 - Clássicos Universais\nNº6 -  Ficção Científica\nNº7 - Drama / Sociedade\nNº8 - Não Ficção\nNº9 - Filosofia / Psicologia\nNº0 - Sair\n--> "))
        os.system("cls")
        if genero > 0 and genero < 10:
            nome_do_livro=input("Nome do livro:\n-->")
            os.system("cls")
            autor=input("Autor do livro:\n-->")
            os.system("cls")
            for livro in biblioteca:
                if (livro.nome.lower()==nome_do_livro.lower()
                    and livro.autor.lower()==autor.lower()
                    and livro.genero==genero):
                    if livro.disponivel:
                        print(f"O livro '{livro.nome}' de {livro.autor} está disponível para empréstimo.")
                        confirmar=input("Deseja emprestar este livro? (Sim/Não): ").strip().lower()
                        if confirmar=="sim":
                            livro.disponivel=False
                            print(f"Você emprestou o livro '{livro.nome}'. Aproveite a leitura!")
                        else:
                            print("Empréstimo cancelado.")
                    else:
                        print(f"Desculpe, o livro '{livro.nome}' de {livro.autor} não está disponível no momento.")
                    break
            else:
                print("Livro não encontrado. Verifique os detalhes e tente novamente.")
            input("Pressione Enter para continuar...")
        elif genero==0:
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
def devolucao(livros):
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
        continuar=input("Deseja devolver outro livro? (Sim/Não): ").strip().lower()
        if continuar!="sim":
            break
