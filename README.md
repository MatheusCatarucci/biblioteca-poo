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
1. Guilherme: Listagem por autor, gênero e livros emprestados;
2. Matheus: Instanciação das classes e formatação lógica
3. Moisés: Adição e edição de livros (SET);
4. Gabriel: Edição e formatação de livros emprestados e devolvidos;
5. João Vitor: Documentação completa do projeto no README.md
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
### 4️⃣: **Contas: ADM e Usuário** 🛠️
#### 4.1: **Contas: ADM** 👤📚
A conta com a função de Administrador será nosso construtor para criar, editar ou remover os livros. Ou seja, a pessoa que tiver o acesso e o poder administrativo desta conta, terá a liberdade para fazer tais funções mencionadas. Além de também poder emprestar, devolver e listar livros.
#### 4.2: **Contas: Usuário** 🧑📚
A conta com a função de usuário só poderá listar, emprestar ou devolver livros. Não será possível fazer a edição, remoção ou criação de livros a não se for um administrador.

