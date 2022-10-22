s1 = 'Brasil Hexa 2006'
s2 = 'Brasil! Hexa 2006!'

print(s1)
print(len(s1))

print(s2)
print(len(s2))

if len(s1) == len(s2):
    print("Possuem o mesmo tamanho.")
else:
    print("As strings possuem tamanhos diferentes.")

if s1 == s2:
    print("As strings inseridas são iguais.")
else:
    print("As strings inseridas são diferentes.")
