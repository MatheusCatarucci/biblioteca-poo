class Livro:
    #Construtor
    def _init_(self, titulo, autor, genero, status):
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
    

Biblioteca = {
    '1': Livro('Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 'Fantasia', True),
    '2': Livro('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia', False),
    '3': Livro('A Guerra dos Tronos', 'George R.R. Martin', 'Fantasia', True)
}