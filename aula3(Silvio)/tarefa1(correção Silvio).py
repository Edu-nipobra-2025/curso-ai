import math as m 

def ler_real(msg: str) -> float:
    while True: 
     try:
        return float(input(msg).replace(",","."))
     except ValueError:
        print("Entrada Inválida")

    
def soma (a: float, b: float) -> float:
           return a+b
def subtra (a: float, b: float) -> float:
           return a-b
def multi (a: float, b: float) -> float:
           return a*b
def div (a: float, b: float) -> float:
           return a/b
     
def main():
 while True:
  print("\n ----Menu----")
  print("\n 1) Adição")
  print("\n 2) Subtração")
  print("\n 3) Multiplicação")
  print("\n 4) Divisão")
  print("\n 0) Fim")
  try:
    opcao = int(input("Escolha sua opção.").strip)
  except ValueError:
    continue 

 if opcao == 0:
     print ("Até Mais!")
break

 if opcao == 1:
    a = int(input("Dê primeiro Valor\n"))
    b = int(input("Dê segundo Valor\n"))
    print(soma(a,b))
 elif opcao == 2:
    a = int(input("Dê primeiro Valor\n"))
    b = int(input("Dê segundo Valor\n"))
    print(subtra(a,b))
 elif opcao == 3:
    a = int(input("Dê primeiro Valor\n"))
    b = int(input("Dê segundo Valor\n"))
    print(multi(a,b))
 elif opcao == 4:
  if b == 0:
   print("Valor inválido!")
  else:
      print(div(a,b))     
