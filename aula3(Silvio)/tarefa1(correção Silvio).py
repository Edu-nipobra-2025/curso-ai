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
if b ==0:
    raise ZeroDivisionError("Erro, divisão por zero")
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

if 1 <= opcao <= 4:
   a = ler_real("Primeiro número: ")
   b = ler_real("Segundo número: ")

if opcao == 1:
        r = soma (a,b)
        print("Resultado:", r)
elif opcao == 2:
        r = subtra (a,b)
        print("Resultado:", r)
elif opcao == 3:
        r = multi (a,b)
        print("Resultado:", r)
else:
     try:
          r = div(a,b)
          print("Resultado:", r)
     except ZeroDivisionError:
          print("Erro, Divisão por zero.")
     else:
      print("Operação inválida.")    
if__name__ == "__main__":
main()