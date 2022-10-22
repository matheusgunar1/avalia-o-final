num1 = float(input("Digite um número:  "))
num2 = float(input("Digite um número:  "))
num3 = float(input("Digite um número:  "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior entre os números digitados!")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior entre os números digitados!")
else:
    print(f"{num3} é o maior entre os números digitados!")

if num1 < num2 and num1 < num3:
    print(f"{num1} é o menor entre os números digitados!")
elif num2 < num1 and num2 < num3:
    print(f"{num2} é o menor entre os números digitados!")
else:
    print(f"{num3} é o menor entre os números digitados!")