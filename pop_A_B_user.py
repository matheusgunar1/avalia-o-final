pop_A_0 = float(input("Digite a primeira população inicial:   "))
tax_A = float(input("Digite a taxa de crescimento ou decrescimento da primeira população:   "))
cres_A = input("A taxa é crescente (A) ou decreescente (B):   ")
pop_B_0 = float(input("Digite a segunda popilação inicial:  "))
tax_B = float(input("Digite a taxa de crescimento ou decrescimento da segunda população:   "))
cres_B = input("A taxa é crescente (A) ou decreescente (B):   ")
t = 0

if cres_A == 'A' and cres_B == 'B':
    pop_A = pop_A_0 + (pop_A_0 * tax_A) * t
    pop_B = pop_B_0 - (pop_B_0 * tax_B) * t
    ti = (pop_B_0 - pop_A_0)/((pop_A_0 * tax_A) + (pop_B_0 * tax_B))
    print(ti)

    if pop_A < pop_B and ti > 0:
        while pop_A < pop_B and ti > 0:
            pop_A = pop_A_0 + (pop_A_0 * tax_A) * t
            print(pop_A)
            pop_B = pop_B_0 - (pop_B_0 * tax_B) * t
            print(pop_B)
            t += 1
            print(t)
    elif ti < 0:
        print("As populações nunca vão se igualar ou se ultrapassar.")

    elif ti == 0:
        print("As populções são iguais no instante inicial.")

    else:
        while pop_B < pop_A and ti > 0:
            pop_A = pop_A_0 + (pop_A_0 * tax_A) * t
            print(pop_A)
            pop_B = pop_B_0 - (pop_B_0 * tax_B) * t
            print(pop_B)
            t += 1
            print(t)

elif cres_A == 'B' and cres_B == 'A':
    pop_A = pop_A_0 - (pop_A_0 * tax_A) * t
    pop_B = pop_B_0 + (pop_B_0 * tax_B) * t
    ti = (-pop_B_0 + pop_A_0) / (-(pop_A_0 * tax_A) + (pop_B_0 * tax_B))
    print(f" t =  {ti}")

    if pop_B > pop_A and ti > 0:
        while pop_B < pop_A and ti > 0:
            pop_A = pop_A_0 + (pop_A_0 * tax_A) * t
            print(pop_A)
            pop_B = pop_B_0 - (pop_B_0 * tax_B) * t
            print(pop_B)
            t += 1
            print(t)
    elif ti < 0:
        print("As populações nunca vão se igualar ou se ultrapassar.")

    elif ti == 0:
        print("As populções são iguais no instante inicial.")

    else:
        while pop_A > pop_B and ti > 0:
            pop_A = pop_A_0 + (pop_A_0 * tax_A) * t
            print(pop_A)
            pop_B = pop_B_0 - (pop_B_0 * tax_B) * t
            print(pop_B)
            t += 1
            print(t)

print(f"portanto, são necessários {t} anos para que a população de A ultrapasse a população de B." )