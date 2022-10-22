usuario = input("Digite seu nome de usuário:    ")
senha = input("Digite sua senha:   ")

while usuario == senha:
    print("Erro! Nome de usuário igual a senha!")
    usuario = input("Digite seu nome de usuário:    ")
    senha = input("Digite sua senha:   ")