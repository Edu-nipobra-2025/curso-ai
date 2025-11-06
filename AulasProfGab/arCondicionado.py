
def funcaoAr(temp):
    temp
    if tempAjudante >= 100:
        print("Ligado!")
    elif tempAjudante <= 90:
        print("Desligado!")
    elif tempAjudante > 90 and tempAjudante < 100:
        print("Ar funcionando seguindo protocolo anterior")
        return  
while True:
 tempAjudante = int(input("Dê o valor da temperatura ambiente"))
 temp = tempAjudante
 print(temp,"")
 if tempAjudante >= 100:
     funcaoAr(temp)
     print("Diminuindo temperatura!")
    
 elif tempAjudante <= 90:
     funcaoAr(temp)
     print("Ligando Ar-Condicionado!")
   
 elif tempAjudante > 90 and tempAjudante < 100:
     funcaoAr(temp)
     print("Ar entre dois estados....")
    