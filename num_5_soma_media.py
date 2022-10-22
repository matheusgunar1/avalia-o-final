num = []
n1 = float(input("Digite um número: "))
num.append(n1)
n2 = float(input("Digite um número: "))
num.append(n2)
n3 = float(input("Digite um número: "))
num.append(n3)
n4 = float(input("Digite um número: "))
num.append(n4)
n5 = float(input("Digite um número: "))
num.append(n5)

media = sum(num, 0)/5

a = sum(num, 0)


print(f'A soma dos números é {a}.')
print(f"A média dos números é {media}.")