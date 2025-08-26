import os
from livros import *


def emprestimos():
    while True:
        os.system("cls")
        print(" _________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |_________|")
        print("")
        genero = int(input("Gêneros Disponiveis:\nNª1 - Ficção Literaria\nNº2 - Fantasia\nNº3 - Mistério / Suspense\nN4º - Romance\nNº5 - Clássicos Universais\nNº6 -  Ficção Científica\nNº7 - Drama / Sociedade\nNº8 - Não Ficção\nNº9 - Filosofia / Psicologia\nNº0 - Sair\n--> "))
        os.system("cls")
        if genero > 0 and genero < 10:
            ListagemPorID()
            id_do_livro=int(input("Insira o ID do livro desejado:\n--> "))
            os.system("cls")
            if Biblioteca[id_do_livro].getStatus() == True:
                conf=input("O Livro está disponível para empréstimo. Confirmar empréstimo? (y/n)\n---> ")
                if conf.lower() == 'y':
                    Biblioteca[id_do_livro].setStatus(False)
                    print(f"Você emprestou o livro ''{Biblioteca[id_do_livro].getTitulo()}''. Aproveite a leitura!")
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
        elif genero == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
            break
        break
def devolucao(livros):
    while True:
        os.system("cls")
        print(" _________\n |                          |\n |                          |\n |     Devolução dos Livros  |\n |                          |\n |_________|")
        print("")
        nome_do_livro = input("Nome do livro que você deseja devolver:\n-->")
        os.system("cls")
        autor = input("Autor do livro que você irá devolver:\n-->")
        os.system("cls")
        for livro in livros:
            if livro.nome.lower() == nome_do_livro.lower() and livro.autor.lower() == autor.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"Você devolveu o livro '{livro.nome}'. Obrigado!")
                else:
                    print(f"O livro '{livro.nome}' já está disponível na biblioteca.")
                break
        else:
            print("Livro não encontrado. Verifique os detalhes e tente novamente.")
        input("Pressione Enter para continuar...")
        break
    
emprestimos()
print('')
ListagemPorID()