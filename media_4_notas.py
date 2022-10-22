notas = []
nota1 = float(input("Digite a primeira nota: "))
notas.append(nota1)
nota2 = float(input("Digite a segunda nota:  "))
notas.append(nota2)
nota3 = float(input("Digite a terceira nota:  "))
notas.append(nota3)
nota4 = float(input("Digite a quarta nota:  "))
notas.append(nota4)

soma = sum(notas, start=0)
media = soma/4

print(f"A média das 4 notas do aluno foi {media}!")