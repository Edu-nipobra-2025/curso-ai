def ler_entrada(mensagem):
 while True:
  try:
       valor = int(input(f"{mensagem} (=0 desligado, 1 ligado)"))
       if valor in(0, 1):
        return valor 
       else:
         print("Digite um número válido")
  except ValueError:
          print("Entrada Inválida")

maquina1 = ler_entrada("Maquina 1")
maquina2 = ler_entrada("Maquina 1")
maquina3 =ler_entrada("Maquina 1")


requerimentos = False
maquinas = [maquina1,maquina2,maquina3]


ligadas = sum(maquinas)
if 4 > ligadas >= 2:
    print("Produzindo")
else:
    print("produção parada")
    faltam = 2 - ligadas
    print(f"É necessário ligar {faltam} máquinas(s)")
    sugestao = []
    for i, estado in enumerate (maquinas):
     if estado == 0:
      sugestao.append(f"máquina {i+1}")
      if len (sugestao) == faltam:
       break
print("sugestão: ", ", ".join(sugestao))