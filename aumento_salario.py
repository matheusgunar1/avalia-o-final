salario_atual = float(input("Qual o salário atual:    "))

if salario_atual <= 280.0:
    aumento = salario_atual + salario_atual * 0.2
    print(f"O salário recebido era de R$ {salario_atual}. \n "
          f"Você recebeu um aumento de 20 % e seu salário passará a ser de R$ {aumento}. ")
elif 280.0 < salario_atual <= 700.0:
    aumento = salario_atual + salario_atual * 0.15
    print(f"O salário recebido era de R$ {salario_atual}. \n "
          f"Você recebeu um aumento de 15 % e seu salário passará a ser de R$ {aumento}. ")
elif 700.0 < salario_atual < 1500.0:
    aumento = salario_atual + salario_atual * 0.10
    print(f"O salário recebido era de R$ {salario_atual}. \n "
          f"Você recebeu um aumento de 10 % e seu salário passará a ser de R$ {aumento}. ")
else:
    aumento = salario_atual + salario_atual * 0.05
    print(f"O salário recebido era de R$ {salario_atual}. \n "
          f"Você recebeu um aumento de 5 % e seu salário passará a ser de R$ {aumento}. ")