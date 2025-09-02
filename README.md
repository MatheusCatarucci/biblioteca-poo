# Projeto Avaliativo: BibliotecaPOO 📚
### 1️⃣: **Introdução** 
Projeto avaliativo de programação back-end em Pyhton onde o objetivo é desenvolver um sistema de biblioteca simples utilizando Programação Orientada a Objetos (POO). Cada livro deve obrigatoriamente possuir um título, autor, gênero literário e status de disponibilidade (emprestado ou não).
### 2️⃣: **Estrutura do Projeto**👨‍💻
A estrutura que iremos usar para fazer o sistema será a seguinte:
#### 2.1: - Livros.py 📖
Usaremos o arquivo "livros.py" para definirmos a classe Livro.
#### 2.2: - funcoes.py 🔧
Utilizaremos o arquivo "funcoes.py" manipular a lista de livros, incluindo::
1. Emprestar;
2. Devolver;
3. Listar livros;
4. Separar por gênero, autor ou livros emprestados.
#### 2.3: - main.py 🚀
Arquivo principal do sistema, onde tudo será condicionado a inicializar a programação usando os outros arquivos.
#### 2.4: - README.md 📃
Documentação completa do projeto. Explicando cada detalhe registrado na programação construída.
### 3️⃣: **Programação do projeto**
4 pessoas programaram o projeto com as seguintes funções declaradas. Uma pessoa fez a documentação. Sendo:
| Nome        | Responsabilidade                                             |
|-------------|--------------------------------------------------------------|
| Guilherme   | Listagem por autor, gênero e livros emprestados              |
| Matheus     | Instanciação das classes e formatação lógica                 |
| Moisés      | Adição e edição de livros (métodos SET)                      |
| Gabriel     | Edição e formatação de livros emprestados e devolvidos       |
| João Vitor  | Documentação completa do projeto no README.md                |
### **Funcionalidades** ⚙️
### 3.1: **Funções Auxiliares**
Essas funções foram criadas para facilitar a busca e organização dos livros dentro do sistema, permitindo filtrar por gênero, autor ou status de empréstimo:
1. `listar_por_genero(lista_livros, genero)` → Retorna todos os livros de um gênero específico;
2. `listar_por_autor(lista_livros, autor)` → Retorna todos os livros de determinado autor;
3. `listar_emprestados(lista_livros)`→ Retorna apenas os livros que estão emprestados.
#### 3.2: **Classes de livros** 📘📗📕📒📔
1. Construtor para criar os livros;
2. Métodos **GET**: acessar título, autor, gênero e situação do livro;
3. Métodos **SET**: atualizar informações do livro;
4. Métodos de **empréstimo e devolução**.
#### 4.2: **Explicando a programação de cada arquivo**
#### **Classes**
A função `class Livro` foi utilizada no arquivo livros.py para ter a organização e definir os GETs/SETs para fazer os acessos/modificações das informações. Além disso, ele permite o controle de status para ver se o livro está disponivel ou emprestado.
#### **GETs e SETs**
**GET:** Usado para pegar/retornar o valor atribuído privado de uma classe.
**SET:** Usado para manipular, ou seja, o SET é quem altera esse valor de forma controlada.
Exemplo: 
```python
def _init_(self, titulo)
    self.__titulo = titulo
# -------------------------
def getTitulo(self):
    return self.__titulo
# -------------------------
def setTitulo(self, novo_titulo):
    self.__titulo = novo_titulo
```
Isto também foi utilizado para "autor", "gênero" e "status".

#### **Uso de Def**

No projeto, foi utilizado para definir funções específicas, sendo no arquivo "funcoes.py". 

**Funcoes.py**

- **Listagem por ID**: Permite localizar e exibir informações de um livro a partir do seu identificador único.
- **Listagem por Autor:** Permite buscar e exibir todos os livros de um determinado autor.
- **Listagem por gênero:** Permite buscar e mostrar os livros por gênero.
- **Listagem por disponíveis:** Faz a busca pelos livros disponíveis.
- **Listagem por emprestados:** Procura quais livros no sistema já foram emprestados.
- **Empréstimos**: Gerencia o processo de empréstimo de livros, atualizando a disponibilidade e registrando os dados do usuário.
- **Devolução:** Faz a função de devolução de livros.
- **Menu:** faz a construção do menu.

### Conclusão 🔚

Concluímos que nosso algorítmo sobre bibliotecas POO (Back-end), sua realização foi realizada e concluida com sucesso, afim de todos os componentes e funções estarem em funcionamento adequado e completo, realizando suas atividades pré definidas apartir das funções (DEFs).

 
