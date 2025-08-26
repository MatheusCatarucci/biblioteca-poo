input(" ____________________________\n |                          |\n |                          |\n |   Empréstimo dos Livros  |\n |                          |\n |__________________________|")
print("")
emprestimo=input("Você deseja emprestar um livro? Digite Sim ou Não: ").strip().lower()
if emprestimo == "sim":
    print("Vamos emprestar um livro!")
    input("Aperte Enter para continuar...")
else:
    print("Tudo bem, até a próxima!")
    