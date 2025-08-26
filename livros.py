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
    def setTitulo(self, novo_titulo):
        self.__titulo = novo_titulo
    def setAutor (self, novo_autor):
        self.__autor = novo_autor
    def setGenero(self, novo_genero):
        self.__genero = novo_genero
    def setStatus (self, novo_status):
        self.__status = novo_status
    

Biblioteca = {
    1: Livro('Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', 'Fantasia', True),
    2: Livro('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 'Fantasia', False),
    3: Livro('A Guerra dos Tronos', 'George R.R. Martin', 'Fantasia', True)
}

def ListagemPorID():
    for chave, Livro in Biblioteca.items():
        if Livro.getStatus() == True:
            print(f"ID: [{chave}] |  Livro Disponível  | Livro: {Livro.getTitulo()} - {Livro.getAutor()}")
        else:
            print(f"ID: [{chave}] | Livro Indisponível | Livro: {Livro.getTitulo()} - {Livro.getAutor()}")

def ListagemAutor():
    for chave, Livro in Biblioteca.items():
        if Livro.getStatus() == True:
            print(f"ID: [{chave}] |  Livro Disponível  | Livro")