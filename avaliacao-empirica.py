import pandas as pd
import numpy as np

dados = pd.read_csv("resultados_huffman.csv")

def estimar_tempo(c, n):
    return c * n * np.log2(n)

# Função para exibir estimativa e erro percentual
def exibir_comparacao(nome_teste, n, tempo_real, c):
    tempo_estimado = estimar_tempo(c, n)
    erro = abs(tempo_estimado - tempo_real) / tempo_real * 100
    print(f"{nome_teste}")
    print(f"  n = {n}")
    print(f"  Tempo real     = {tempo_real:.4f} s")
    print(f"  Tempo estimado = {tempo_estimado:.4f} s")
    print(f"  Diferença relativa = {erro:.2f}%\n")

# ===============================
# Estimativa baseada no maior n
# ===============================
print("=== Estimativa baseada no maior n medido ===")
n_maior = dados["Tamanho_entrada"].iloc[-1]
tempo_maior = dados["Tempo_execucao"].iloc[-1]
constante = tempo_maior / (n_maior * np.log2(n_maior))
print(f"Constante c estimada ≈ {constante:.10f}\n")

n_dobro = 2 * n_maior
tempo_estimado_dobro = estimar_tempo(constante, n_dobro)
print(f"Estimativa para 2n = {n_dobro}")
print(f"  Tempo estimado ≈ {tempo_estimado_dobro:.4f} s\n")

exibir_comparacao("Teste com penúltimo n", 
                  dados["Tamanho_entrada"].iloc[-2],
                  dados["Tempo_execucao"].iloc[-2],
                  constante)

exibir_comparacao("Teste com antepenúltimo n", 
                  dados["Tamanho_entrada"].iloc[-3],
                  dados["Tempo_execucao"].iloc[-3],
                  constante)

exibir_comparacao("Teste com n anterior ao antepenúltimo", 
                  dados["Tamanho_entrada"].iloc[-4],
                  dados["Tempo_execucao"].iloc[-4],
                  constante)

# ===============================
# Nova estimativa baseada no penúltimo n
# ===============================
print("=== Nova estimativa com base no penúltimo n ===")
n_ref = dados["Tamanho_entrada"].iloc[-2]
tempo_ref = dados["Tempo_execucao"].iloc[-2]
tempo_real_2n = dados["Tempo_execucao"].iloc[-1]
nova_constante = tempo_ref / (n_ref * np.log2(n_ref))

n_dobro_ref = 2 * n_ref
tempo_estimado_2n = estimar_tempo(nova_constante, n_dobro_ref)

print(f"Constante c (base penúltimo n) ≈ {nova_constante:.10f}")
print(f"Estimativa para 2n = {n_dobro_ref}")
print(f"  Tempo estimado ≈ {tempo_estimado_2n:.4f} s")
print(f"  Tempo real     ≈ {tempo_real_2n:.4f} s")
erro = abs(tempo_estimado_2n - tempo_real_2n) / tempo_real_2n * 100
print(f"  Erro percentual ≈ {erro:.2f}%\n")
