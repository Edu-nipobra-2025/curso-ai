def media(a,b,c):
 mediana = (a+b+c)/ 3 
 print(mediana)
 return mediana


a = int(input("dê primeira nota\n"))
b = int(input("dê segunda nota\n"))
c = int(input("dê terceira nota\n"))

media(a,b,c)
if media(a,b,c) >= 7:
 print("aprovado")
else:
 print("reprovado!")