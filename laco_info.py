nome = input("Digite seu nome:   ")
idade = int(input("Digite sua idade:   "))
salario = float(input("Digite seu salário:   "))
sexo = input("Qual seu sexo (f - feminino e m - masculino):   ").lower()
estado_civil = input("Qual seu estado civil (s - solteiro, c - casado, d - divorciado e v - viúvo:    ").lower()

while len(nome) < 3:
    print("Erro!!! Nome muito pequeno, menos de 4 caracteres! ")
    nome = input("Digite seu nome:   ")

while 0 > idade or idade > 150:
    print("Erro! Idade inválida.")
    idade = int(input("Digite sua idade:   "))

while sexo != 'm' and sexo != 'f':
    print("Erro! Valor inválido de sexo.")
    sexo = input("Qual seu sexo (f - feminino e m - masculino:   ").lower()

while salario < 0:
    print("Erro! Valor inválido de salário.")
    salario = float(input("Digite seu salário:   "))

while estado_civil != 'c' and estado_civil != 's' and estado_civil != 'd' and estado_civil != 'v':
    print("Erro! Estado civil inválido.")
    estado_civil = input("Qual seu estado civil (s - solteiro, c - casado, d - divorciado e v - viúvo:    ").lower()

print("Todas as informações fornecidas são válidas!!!")
