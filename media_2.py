notas = []

nota1 = float(input("Digite a primeira nota: "))
notas.append(nota1)
nota2 = float(input("Digite a segunda nota:  "))
notas.append(nota2)

media = sum(notas, start=0)/2

if media >= 7 and media != 10:
    print("Aprovado!")
elif media == 10:
    print("Aprovado com distinção!!!")
else:
    print("Reprovado.")
