nome = str(input("Digite seu nome: "))
no = list(nome)
i = 0
for i in range(0, len(nome)+1):
    print(nome[:i])