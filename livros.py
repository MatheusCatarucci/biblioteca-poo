class Livro:
    #Construtor -> Define os atributos -> Propriedades
    def __init__(self, nome, autor, genero, status):

        self.__nome = nome
        self.__autor = autor
        self.__genero = genero
        self.__status = status
    # -----------------------------------------------------------------------
    # Métodos -> 
    def getNome(self):
        return self.__nome
    def getAutor(self):
        return self.__autor
    def getGenero(self):
        return self.__genero
    def getStatus(self):
        return self.__status
    # -----------------------------------------------------------------------
    # Set's

    # -----------------------------------------------------------------------
biblioteca = {
    # Ficção Literária
    1 : Livro("Dom Casmurro", "Machado de Assis", "Ficção Literária", True),
    2 : Livro("Grande Sertão: Veredas", "Guimarães Rosa", "Ficção Literária", True),
    3 : Livro("Cem Anos de Solidão", "Gabriel García Márquez", "Ficção Literária", True),
    
    # Fantasia
    4 : Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", True),
    5 : Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", True),
    6 : Livro("A Guerra dos Tronos", "George R.R. Martin", "Fantasia", True),
    
    # Mistério / Suspense
    7 : Livro("Assassinato no Expresso do Oriente", "Agatha Christie", "Mistério / Suspense", True),
    8 : Livro("O Iluminado", "Stephen King", "Terror / Suspense", True),
    9 : Livro("O Código Da Vinci", "Dan Brown", "Mistério / Suspense", True),
    
    # Clássicos Universais
    10 : Livro("1984", "George Orwell", "Clássicos Universais", True),
    11 : Livro("O Apanhador no Campo de Centeio", "J.D. Salinger", "Clássicos Universais",True),
    12 : Livro("Moby Dick", "Herman Melville", "Clássicos Universais", True),
    
    # Romance
    13 : Livro("Orgulho e Preconceito", "Jane Austen", "Romance", True),
    14 : Livro("Anna Kariênina", "Liev Tolstói", "Romance", True),
    15 : Livro("Eleanor & Park", "Rainbow Rowell", "Romance Jovem Adulto", True),
    
    # Ficção Científica
    16 : Livro("Duna", "Frank Herbert", "Ficção Científica", True),
    17 : Livro("Neuromancer", "William Gibson", "Cyberpunk", True),
    18 : Livro("Fundação", "Isaac Asimov", "Ficção Científica", True),
    
    # Drama / Sociedade
    19 : Livro("O Sol é para Todos", "Harper Lee", "Drama / Sociedade", True),
    20 : Livro("A Metamorfose", "Franz Kafka", "Existencialismo", True),
    
    # 📓 Não Ficção
    21 : Livro("Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", "História / Antropologia", True),
    22 : Livro("A Arte da Guerra", "Sun Tzu", "Estratégia", True),
    23 : Livro("O Diário de Anne Frank", "Anne Frank", "Memórias", True),
    
    # Filosofia / Psicologia
    24 : Livro("Assim Falou Zaratustra", "Friedrich Nietzsche", "Filosofia", True),
    25 : Livro("O Mal-Estar na Civilização", "Sigmund Freud", "Psicologia", True),
}
