data = str(input("Digite sua data de nascimento:  "))
a = list(data)

if '/01/' in data:
    print(f"{a[0]}{a[1]} de Janeiro de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/02/' in data:
    print(f"{a[0]}{a[1]} de Fevereiro de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/03/' in data:
    print(f"{a[0]}{a[1]} de Março de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/04/' in data:
    print(f"{a[0]}{a[1]} de Abril de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/05/' in data:
    print(f"{a[0]}{a[1]} de Maio de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/06/' in data:
    print(f"{a[0]}{a[1]} de Junho de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/07/' in data:
    print(f"{a[0]}{a[1]} de Julho de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/08/' in data:
    print(f"{a[0]}{a[1]} de Agosto de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/09/' in data:
    print(f"{a[0]}{a[1]} de Setembro de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/10/' in data:
    print(f"{a[0]}{a[1]} de Outubro de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/11/' in data:
    print(f"{a[0]}{a[1]} de Novembro de {a[6]}{a[7]}{a[8]}{a[9]}")
elif '/12/' in data:
    print(f"{a[0]}{a[1]} de Dezembro de {a[6]}{a[7]}{a[8]}{a[9]}")