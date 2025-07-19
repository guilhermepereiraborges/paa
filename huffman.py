import heapq
import random
import time
import pandas as pd

# --------------------------
# ESTRUTURA DO NÓ
# --------------------------

class Node:
    def __init__(self, simbolo, freq):
        self.simbolo = simbolo
        self.freq = freq
        self.esquerda = None
        self.direita = None

    def __lt__(self, other):
        return self.freq < other.freq

# --------------------------
# ALGORITMO DE HUFFMAN
# --------------------------

def construir_arvore_huffman(simbolos, frequencias):
    heap = [Node(s, f) for s, f in zip(simbolos, frequencias)]
    heapq.heapify(heap)

    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        z = Node(None, x.freq + y.freq)
        z.esquerda = x
        z.direita = y
        heapq.heappush(heap, z)

    return heap[0]

def gerar_codigos(nodo, prefixo='', codigos=None):
    if codigos is None:
        codigos = {}
    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = prefixo
    else:
        gerar_codigos(nodo.esquerda, prefixo + '0', codigos)
        gerar_codigos(nodo.direita, prefixo + '1', codigos)
    return codigos

# --------------------------
# EXECUÇÃO E SALVAMENTO
# --------------------------

resultados = []
tamanho = 10
max_tamanho = 10**7

while tamanho <= max_tamanho:

    entrada = [str(i) for i in range(tamanho)]
    random.shuffle(entrada)

    frequencias = {}
    for c in entrada:
        frequencias[c] = frequencias.get(c, 0) + 1

    simbolos = list(frequencias.keys())
    pesos = list(frequencias.values())

    inicio = time.perf_counter()
    raiz = construir_arvore_huffman(simbolos, pesos)
    codigos = gerar_codigos(raiz)
    fim = time.perf_counter()

    tempo_execucao = fim - inicio
    resultados.append((tamanho, tempo_execucao))
    tamanho *= 2

df = pd.DataFrame(resultados, columns=['Tamanho_entrada', 'Tempo_execucao'])
df.to_csv('resultados_huffman.csv', index=False)
print("Arquivo 'resultados_huffman.csv' salvo com sucesso.")