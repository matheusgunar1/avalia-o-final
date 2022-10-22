preco1 = float(input("Digite o preço de um produto em R$:  "))
preco2 = float(input("Digite o preço de um produto em R$:  "))
preco3 = float(input("Digite o preço de um produto em R$:  "))

if preco1 < preco2 and preco1 < preco3:
    print("Comprar produto 1.")
elif preco2 < preco1 and preco2 < preco3:
    print("Comprar produto 2.")
else:
    print("Comprar produto 3.")
