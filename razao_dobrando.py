import pandas as pd
import numpy as np

df = pd.read_csv("resultados_huffman.csv")

n = df["Tamanho_entrada"].iloc[-1]
Tn = df["Tempo_execucao"].iloc[-1]

c = Tn / (n * np.log2(n))

n2 = 2 * n
Tn2_estimado = c * n2 * np.log2(n2)

print(f"Último n = {n}")
print(f"T(n) = {Tn:.4f} s")
print(f"Constante c ≈ {c:.10f}")
print(f"T(2n) estimado ≈ {Tn2_estimado:.4f} s \n")

penultimo = df["Tamanho_entrada"].iloc[-2]
penultimo_tempo = df["Tempo_execucao"].iloc[-2]

res_teste = c * penultimo * np.log2(penultimo)

print(f"Tempo estimado para n = {penultimo} é {res_teste:.4f} s")
print(f"Tempo real para n = {penultimo} é {penultimo_tempo:.4f} s")

dif_rel = (abs(res_teste - penultimo_tempo) / penultimo_tempo) * 100
print(f"Razão entre tempo estimado e real: {dif_rel:.2f}%")