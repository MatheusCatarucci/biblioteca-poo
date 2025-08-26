import os
from classes import *
def empretimos(livros):
    while True:
        os.system("cls")
        print(" ____________________________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |__________________________|")
        print("")
        genero = int(input("Informe o Genero do livro em que você procura\nNª1 - Ficção Literaria\nNº2 - Fantasia\nNº3 - Mistério / Suspense\nN4º - Romance\nNº5 - Clássicos Universais\nNº6 -  Ficção Científica\nNº7 - Drama / Sociedade\nNº8 - Não Ficção\nNº9 - Filosofia / Psicologia\nNº0 - Sair\n--> "))
        os.system("cls")
        if genero > 0 and genero < 10:
            nome_do_livro = input("Nome do livro:\n-->")
            os.system("cls")
            genero_do_livro = input("Gênero do livro:\n-->")
            os.system("cls")
            autor = input("Autor do livro:\n-->")
            os.system("cls")
            for livro in livros:
                if livro.nome.lower() == nome_do_livro.lower() and livro.autor.lower() == autor.lower() and livro.genero.lower() == genero_do_livro.lower():
                    if livro.disponivel:
                        print(f"O livro '{livro.nome}' de {livro.autor} está disponível para empréstimo.")
                        confirmar = input("Deseja emprestar este livro? (Sim/Não): ").strip().lower()
                        if confirmar == "sim":
                            livro.disponivel = False
                            print(f"Você emprestou o livro '{livro.nome}'. Aproveite a leitura!")
                        else:
                            print("Empréstimo cancelado.")
                    else:
                        print(f"Desculpe, o livro '{livro.nome}' de {livro.autor} não está disponível no momento.")
                    break