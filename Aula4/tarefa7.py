val = int(input("Digite um valor:"))

if val < 2:
    print("não é primo!")
else:
    eh_primo = True
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("é primo!")
    else:
        print("não é primo!")