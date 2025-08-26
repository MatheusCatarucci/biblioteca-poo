class Livro:
    #Construtor -> Define os atributos -> Propriedades
    def __init__(self, titulo, autor, genero, status):

        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__status = status
    # -----------------------------------------------------------------------
    # Métodos -> Definem os 
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

Biblioteca = {
    # Ficção Literária
    1 : Livro(nome="Dom Casmurro", autor="Machado de Assis", genero="Ficção Literária", status=True),
    2 : Livro(nome="Grande Sertão: Veredas", autor="Guimarães Rosa", genero="Ficção Literária", status=True),
    3 : Livro(nome="Cem Anos de Solidão", autor="Gabriel García Márquez", genero="Ficção Literária", status=True),
    
    # Fantasia
    4 : Livro(nome="O Senhor dos Anéis: A Sociedade do Anel", autor="J.R.R. Tolkien", genero="Fantasia", status=True),
    5 : Livro(nome="Harry Potter e a Pedra Filosofal", autor="J.K. Rowling", genero="Fantasia", status=True),
    6 : Livro(nome="A Guerra dos Tronos", autor="George R.R. Martin", genero="Fantasia", status=True),
    
    # Mistério / Suspense
    7 : Livro(nome="Assassinato no Expresso do Oriente", autor="Agatha Christie", genero="Mistério / Suspense", status=True),
    8 : Livro(nome="O Iluminado", autor="Stephen King", genero="Terror / Suspense", status=True),
    9 : Livro(nome="O Código Da Vinci", autor="Dan Brown", genero="Mistério / Suspense", status=True),
    
    # Clássicos Universais
    10 : Livro(nome="1984", autor="George Orwell", genero="Clássicos Universais", status=True),
    11 : Livro(nome="O Apanhador no Campo de Centeio", autor="J.D. Salinger", genero="Clássicos Universais", status=True),
    12 : Livro(nome="Moby Dick", autor="Herman Melville", genero="Clássicos Universais", status=True),
    
    # Romance
    13 : Livro(nome="Orgulho e Preconceito", autor="Jane Austen", genero="Romance", status=True),
    14 : Livro(nome="Anna Kariênina", autor="Liev Tolstói", genero="Romance", status=True),
    15 : Livro(nome="Eleanor & Park", autor="Rainbow Rowell", genero="Romance Jovem Adulto", status=True),
    
    # Ficção Científica
    16 : Livro(nome="Duna", autor="Frank Herbert", genero="Ficção Científica", status=True),
    17 : Livro(nome="Neuromancer", autor="William Gibson", genero="Cyberpunk", status=True),
    18 : Livro(nome="Fundação", autor="Isaac Asimov", genero="Ficção Científica", status=True),
    
    # Drama / Sociedade
    19 : Livro(nome="O Sol é para Todos", autor="Harper Lee", genero="Drama / Sociedade", status=True),
    20 : Livro(nome="A Metamorfose", autor="Franz Kafka", genero="Existencialismo", status=True),
    
    # 📓 Não Ficção
    21 : Livro(nome="Sapiens: Uma Breve História da Humanidade", autor="Yuval Noah Harari", genero="História / Antropologia", status=True),
    22 : Livro(nome="A Arte da Guerra", autor="Sun Tzu", genero="Estratégia", status=True),
    23 : Livro(nome="O Diário de Anne Frank", autor="Anne Frank", genero="Memórias", status=True),
    
    # Filosofia / Psicologia
    24 : Livro(nome="Assim Falou Zaratustra", autor="Friedrich Nietzsche", genero="Filosofia", status=True),
    25 : Livro(nome="O Mal-Estar na Civilização", autor="Sigmund Freud", genero="Psicologia", status=True),
}
