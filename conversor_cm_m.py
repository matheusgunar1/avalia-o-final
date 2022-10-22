resp = input("Deseja converter valores de cm em metros (opção A) ou de metros em cm (opção B):  ")
if resp == 'A':
    cm = float(input("Digite um valor em cm: "))
    conversor1 = cm * (1/100)
    print(f" {cm} cm equivalem a {conversor1} m.")
else:
    m = float(input("digite um valor em metros:  "))
    conversor2 = m * 100
    print(f" {m} m equivalem a {conversor2} cm.")
