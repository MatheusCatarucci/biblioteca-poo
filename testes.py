import os
from livros import Livro  # Supondo que a classe Livro está aqui

# Exemplo de biblioteca inicial
biblioteca = [
    Livro("Dom Casmurro", "Machado de Assis", "Ficção Literaria", True),
    Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", True),
    Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Clássicos Universais", True),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", True)
]

# Função para buscar livro
def buscar_livro(nome, autor, livros):
    for livro in livros:
        if livro.getTitulo().lower() == nome.lower() and livro.getAutor().lower() == autor.lower():
            return livro
    return None

# Função de empréstimo
def emprestimos(biblioteca):
    while True:
        os.system("cls")
        print(" _________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |_________|")
        print("")
        genero = int(input(
            "Gêneros Disponíveis:\n"
            "1 - Ficção Literaria\n"
            "2 - Fantasia\n"
            "3 - Mistério / Suspense\n"
            "4 - Romance\n"
            "5 - Clássicos Universais\n"
            "6 - Ficção Científica\n"
            "7 - Drama / Sociedade\n"
            "8 - Não Ficção\n"
            "9 - Filosofia / Psicologia\n"
            "0 - Sair\n--> "
        ))

        if genero == 0:
            break
        elif 1 <= genero <= 9:
            # Mapear número do gênero para nome
            generos = {
                1: "Ficção Literaria",
                2: "Fantasia",
                3: "Mistério / Suspense",
                4: "Romance",
                5: "Clássicos Universais",
                6: "Ficção Científica",
                7: "Drama / Sociedade",
                8: "Não Ficção",
                9: "Filosofia / Psicologia"
            }
            genero_escolhido = generos[genero]

            # Mostrar livros disponíveis desse gênero
            livros_disponiveis = [l for l in biblioteca if l.getGenero().lower() == genero_escolhido.lower() and l.disponivel]
            if livros_disponiveis:
                print(f"\nLivros disponíveis em '{genero_escolhido}':")
                for l in livros_disponiveis:
                    print(f"- {l.getTitulo()} ({l.getAutor()})")
            else:
                print(f"\nNão há livros disponíveis em '{genero_escolhido}' no momento.")
            
            nome_do_livro = input("\nDigite o nome do livro que deseja emprestar:\n--> ")
            autor = input("Digite o autor do livro:\n--> ")

            livro = buscar_livro(nome_do_livro, autor, biblioteca)
            if livro:
                if livro.disponivel:
                    confirmar = input(f"O livro '{livro.getTitulo()}' está disponível. Deseja emprestar? (Sim/Não): ").strip().lower()
                    if confirmar == "sim":
                        livro.disponivel = False
                        print(f"Você emprestou o livro '{livro.getTitulo()}'. Aproveite a leitura!")
                    else:
                        print("Empréstimo cancelado.")
                else:
                    print(f"Desculpe, o livro '{livro.getTitulo()}' já está emprestado.")
            else:
                print("Livro não encontrado. Verifique os detalhes e tente novamente.")

            input("\nPressione Enter para continuar...")

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

# Função de devolução
def devolucao(biblioteca):
    while True:
        os.system("cls")
        print(" _________\n |                          |\n |                          |\n |     Devolução dos Livros  |\n |                          |\n |_________|")
        print("")
        nome_do_livro = input("Nome do livro que deseja devolver:\n--> ")
        autor = input("Autor do livro:\n--> ")

        livro = buscar_livro(nome_do_livro, autor, biblioteca)
        if livro:
            if not livro.disponivel:
                livro.disponivel = True
                print(f"Você devolveu o livro '{livro.getTitulo()}'. Obrigado!")
            else:
                print(f"O livro '{livro.getTitulo()}' já estava disponível na biblioteca.")
        else:
            print("Livro não encontrado. Verifique os detalhes e tente novamente.")

        input("\nPressione Enter para continuar...")
        break

# Exemplo de uso
emprestimos(biblioteca)
