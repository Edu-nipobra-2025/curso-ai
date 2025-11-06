print ("Digiet a temperatura ideal:")
T = input()
T = float(T)
#T = float(input("Digite a temperatura ideal:"))
while True:
    print ("Digite a temperatura do ambiente:")
    temperatura = input()
    temperatura = float(temperatura)

    if temperatura > T:
       print("Acione o ar condicionado")
    elif temperatura < T * 0.9:
       print("Desligue o ar condicionado")