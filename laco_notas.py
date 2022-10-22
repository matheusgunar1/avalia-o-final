nota = float(input("Digite sua nota entre zero e dez:   "))

while nota < 0.0 or nota > 10.0:
    print("Valor Inválido!!!")
    nota = float(input("Digite sua nota entre zero e dez:   "))
