t = 0
pop_A = 80000 + 2400 * t
pop_B = 200000 - 3000 * t
pop_A < pop_B
ti = (200000 - 80000)/(2400 + 3000)
print(ti)

while pop_A < pop_B and ti > 0:
    pop_A = 80000 + 2400 * t
    print(pop_A)
    pop_B = 200000 - 3000 * t
    print(pop_B)
    t += 1
    print(t)

print(f"portanto, são necessários {t} anos para que a população de A ultrapasse a população de B." )
