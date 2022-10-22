turno = input("Em qual turno você estuda?  Matutino (M); Vespertino (V) ou Noturno (N):    ").upper()

if turno == 'M':
    print("Bom dia!!!")
elif turno == 'V':
    print("Boa Tarde!!!")
elif turno == 'N':
    print("Boa Noite!!!")
else:
    print("Valor Inválido!!!")
