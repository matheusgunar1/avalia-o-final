string = str(input("Digite uma frase:  "))
a = list(string)
vogal = 0
espaco = 0

for letra in string:
    if letra == " ":
        espaco += 1
    elif letra in "aAeEiIoOuUãÃõÕáÁéÉêÊíÍóÓúÚàÀ":
        vogal += 1

print(f"A string informada possui {espaco} espaços e {vogal} vogais.")


