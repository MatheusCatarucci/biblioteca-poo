<<<<<<< HEAD
class Livro:
    #Construtor
    def __init__(self, titulo, autor, genero, status):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__status = status
    # -----------------------------------------------------------------------
    # Métodos
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getGenero(self):
        return self.__genero
    def getStatus(self):
        return self.__status
    
livros = {Livro('Senhor dos Anéis', 'J. R. R. Tolkien', 'Ficção', 0)}
print(livros.getAutor())
=======
input(" ____________________________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |__________________________|")
print("")
emprestimo=input("Você deseja emprestar um livro? Digite Sim ou Não: ").strip().lower()
if emprestimo == "sim":
    print("Vamos emprestar um livro!")
    input("Aperte Enter para continuar...")
else:
    print("Tudo bem, até a próxima!")
    
>>>>>>> 4849da74f3f497f5906bcd66b20d4536794f76ae
