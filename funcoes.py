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