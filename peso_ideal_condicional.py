resp = input("Você é homem (A) ou mulher (B)?  ")

if resp == 'A':
    h = float(input("Qual a sua altura em m?  "))
    peso_ideal = (72.7 * h) - 58
    print(f"Seu peso ideal é {peso_ideal} unidades de massa.")
else:
    h = float(input("Qual a sua altura em m?  "))
    peso_ideal = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {peso_ideal} unidades de massa.")
