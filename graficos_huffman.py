import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np  

from avaliacao_empirica import estimar_tempo

dados = pd.read_csv('resultados_huffman.csv')

# Estima a constante com base no maior n
n_maior = dados["Tamanho_entrada"].iloc[-1]
tempo_maior = dados["Tempo_execucao"].iloc[-1]
constante = tempo_maior / (n_maior * np.log2(n_maior))

# Calcula tempos estimados e erro
dados['Tempo_estimado'] = estimar_tempo(constante, dados['Tamanho_entrada'])
dados['Erro_percentual'] = abs(dados['Tempo_estimado'] - dados['Tempo_execucao']) / dados['Tempo_execucao'] * 100

# Configurações de estilo
sns.set(style="whitegrid")

# === 1. Tempo de execução real vs tamanho da entrada ===
plt.figure(figsize=(10, 6))
sns.lineplot(data=dados, x='Tamanho_entrada', y='Tempo_execucao', marker='o', label='Tempo real')
plt.title('Tempo de Execução Real vs Tamanho da Entrada')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Tempo de Execução (s)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()

# === 2. Tempo estimado vs tempo real ===
plt.figure(figsize=(10, 6))
plt.plot(dados['Tamanho_entrada'], dados['Tempo_execucao'], marker='o', label='Tempo real')
plt.plot(dados['Tamanho_entrada'], dados['Tempo_estimado'], marker='s', label='Tempo estimado (c·n·log₂n)')
plt.title('Tempo Real vs Tempo Estimado')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Tempo (s)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show()

# === 3. Erro percentual ===
plt.figure(figsize=(10, 6))
sns.lineplot(x='Tamanho_entrada', y='Erro_percentual', data=dados, marker='o', color='red')
plt.title('Erro Percentual entre Tempo Real e Estimado')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Erro Percentual (%)')
plt.xscale('log')
plt.tight_layout()
plt.show()
