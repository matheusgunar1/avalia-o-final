num1 = float(input("Digite um número qualquer:  "))
num2 = float(input("Digite um número qualquer:  "))

if num1 > num2:
    print(f"O maior número entre os dois digitados foi {num1}.")
elif num1 < num2:
    print(f"O maior número entre os dois digitados foi {num2}.")
else:
    print("Os números digitados são iguais.")