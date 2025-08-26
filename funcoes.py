class Livros:
    def __init__(self, titulo, autor, genero, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponivel = disponivel

# ----------------------------------------------------------------------------------------------------------------------------
    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo
    
    def set_autor (self, novo_autor):
        self.autor = novo_autor

    def set_genero(self, novo_genero):
        self.set_genero = novo_genero

    def set_disponivel (self, status):
        self.disponivel = status