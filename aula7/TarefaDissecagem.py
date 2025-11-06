#CSV na prática → csv.Sniffer, leitura, limpeza e escrita.  
#CSV = Comma Separated Values, valores separados por linha, Armazena dois tabulares.
from __future__ import annotations
#Importa anotação guardadas em strings do que em variáveis
from typing import Optional
#importa tipagem opcional ou nenhuma de uma variável.

def ler_int(msg: str = "Digite um inteiro: ") -> int:
    while True:
        s = input(msg).strip()
        try:
            return int(s)
        except ValueError:
            print("Entrada inválida. Tente novamente.")
#Objeto que Lê um inteiro que manda uma mensagem tipo string "digite um inteiro", que em loop irá retornar a variável "s" que tem um input de mensagem 
# em strip.
#caso dê erro (ValueError) a mensagem será inutilziada e irá voltar devolta ao loop (While True:)
def ler_float_intervalo(
    msg: str = "Valor (0–1): ",
    minimo: float = 0.0,
    maximo: float = 1.0
) -> float:
    while True:
        s = input(msg).strip().replace(",", ".")
        try:
            v = float(s)
            if minimo <= v <= maximo:
                return v
            print(f"Fora do intervalo [{minimo}, {maximo}].")
        except ValueError:
            print("Número inválido.")
        
        #Lê um float em um intervalo minimo de 0.0 Se máximo de 1.0 S que quando verdade (Loop) irá ler uma mensagem string de valor 0-1 a partir
        #duma variável s, sendo a variável v o float de S que se o mínimo for menor que V sendo v menor que o máximo, irá retornar a mesma
        # como "fora do intervalo", com o ValueError de um valor inválido.

def normaliza_nome(nome: str) -> str:
    return " ".join(p.capitalize() for p in nome.strip().split())
#define um objeto chamado normaliza_nome que lê uma string que volta um nome corrigido pelo p.capitalize(), corringindo um nome com uma capitalização.
# e separando os nomes por um split()
def aceita_nao_vazio(s: Optional[str]) -> bool:
    return isinstance(s, str) and s.strip() != ""
# o código traz um s em string opcional com uma booleana, retornando um isinstance com S e uma string, fatiando em um s.strip se não for vazia
# aparente pelo !=""
def coerco_float_br(x: str) -> float:
    return float(x.strip().replace(",", "."))
#puxa um x com uma string do tipo float e retorna um float dividindo o x e trocando as vírgulas por ponto
def valida_intervalo(v: float, minimo: float, maximo: float) -> bool:
    return minimo <= v <= maximo  
#traz um def com requerimentos v Float minimo float e maximo float com uma booleana, retornando 
#minimo menor ou igual v que é menor e igual a máximo