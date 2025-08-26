class Livros:
    def __init__(self, titulo, autor, genero, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._disponivel = disponivel

# ----------------------------------------------------------------------------------------------------------------------------
    def set_titulo(self, novo_titulo):
        self._titulo = novo_titulo
    
    def set_autor (self, novo_autor):
        self._autor = novo_autor

    def set_genero(self, novo_genero):
        self._genero = novo_genero

    def set_disponivel (self, status):
        self._disponivel = status