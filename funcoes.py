import os
from livros import biblioteca

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def ListagemPorID():
    for chave, Livro in biblioteca.items():
        if Livro.getStatus():
            print(f"ID: [{chave}] |  Livro Disponível  | Livro: {Livro.getNome()} - {Livro.getAutor()}")
        else:
            print(f"ID: [{chave}] | Livro Indisponível | Livro: {Livro.getNome()} - {Livro.getAutor()}")

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
            conf = input("O Livro está disponível para empréstimo. Confirmar empréstimo? (y/n)\n---> ")
            if conf.lower() == 'y':
                biblioteca[id_do_livro].setStatus(False)
                print(f"Você emprestou o livro ''{biblioteca[id_do_livro].getNome()}''. Aproveite a leitura!")
                os.system('pause')
            elif conf.lower() == 'n':
                print("Saindo...")
                os.system('pause')
            else:
                print("Nenhuma opção válida selecionada, saindo...")
                os.system('pause')
        else:
            print("Livro indisponível para empréstimo.")
            input("Pressione Enter para continuar...")
        break
    
def devolucao():
    while True:
        limpar_tela()
        print(" === Devolução de Livros === ")
        nome_do_livro = input("Nome do livro que você deseja devolver:\n--> ")
        limpar_tela()
        autor = input("Autor do livro que você irá devolver:\n--> ")
        limpar_tela()
        achado = False
        for Livro in biblioteca.values():
            if Livro.getNome().lower() == nome_do_livro.lower() and Livro.getAutor().lower() == autor.lower():
                achado = True
                if not Livro.getStatus():
                    Livro.setStatus(True)
                    print(f"Você devolveu o livro '{Livro.getNome()}'. Obrigado!")
                else:
                    print(f"O livro '{Livro.getNome()}' já está disponível na biblioteca.")
                break
        if not achado:
            print("Livro não encontrado. Verifique os detalhes e tente novamente.")
        input("Pressione Enter para continuar...")

        continuar = input("Deseja devolver outro livro? (Sim/Não): ").strip().lower()
        if continuar != "sim":
            break

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
