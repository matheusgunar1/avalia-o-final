letra = input("Digite uma letra:  ")

def vogal(v):
    if v in "aAeEiIOoUu":
        return "Vogal"
    else:
        return "Consoante"

print(vogal(letra))



