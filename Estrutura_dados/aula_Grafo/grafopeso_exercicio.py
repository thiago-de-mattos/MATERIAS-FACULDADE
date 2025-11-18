import matplotlib.pyplot as plt
import networkx as nx
# =========================
# PARTE 1 — REPRESENTAÇÃO
# =========================

# 1) Defina suas cidades (mínimo 3). Usei 4 para o exemplo.

cidades = []
cidades_escolhas = input(int('digite a quantidade de cidades que vôce quer adicionar'))

for cidade in range(cidades_escolhas):
    nome_cidade = input(str('Digite o nome da cidade: '))
    cidades.append(nome_cidade)

    

cidades_destinos = input('digite a cidade de destino: ')

for cidade in cidades:
    if not cidades_destinos == cidade:
        print('cidade não registrada!!!')
    else:
        peso_vertices = input(int('digite o valor de peso das vertices: '))

    estradas = (cidade, cidades_destinos, {'weight': peso_vertices})

    
# 2) Crie o grafo direcionado
G = nx.DiGraph()
G.add_nodes_from(cidades)

# 3) Estradas (arestas) com custos (peso = tempo/distância/custo)
#    Formato: (origem, destino, {"weight": custo})

G.add_edges_from(estradas)

# 4) Posição fixa dos nós (só para o desenho ficar legível)
pos = {
    'Armazem': (0.1, 0.6),
    'CidadeA': (0.45, 0.9),
    'CidadeB': (0.45, 0.3),
    'CidadeC': (0.85, 0.6),
}

# 5) Desenhar o grafo com os custos nas arestas
def desenhar_grafo(grafo, titulo):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_aspect('equal')
    nx.draw_networkx_nodes(grafo, pos, node_color='#A7D0E8', edgecolors='k',
                           node_size=1800, linewidths=1.8, ax=ax)
    nx.draw_networkx_labels(grafo, pos, font_size=12, font_weight='bold', ax=ax)
    nx.draw_networkx_edges(grafo, pos, arrows=True, arrowstyle='-|>', arrowsize=24,
                           width=2, edge_color='black', ax=ax)
    # rótulos de pesos
    edge_labels = {(u, v): d['weight'] for u, v, d in grafo.edges(data=True)}
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels, font_size=11, ax=ax)
    plt.title(titulo, pad=10)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

desenhar_grafo(G, 'Rede de Cidades (Custos nas estradas)')

# =========================
# PARTE 2 — CAMINHO MÍNIMO (MANUAL)
# =========================

# Função simples que soma o custo de um caminho (lista de nós)
def custo_caminho(grafo, caminho):
    # Ex.: caminho = ['Armazem', 'CidadeA', 'CidadeC']
    total = 0
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i+1]
        if grafo.has_edge(u, v):
            total += grafo[u][v]['weight']
        else:
            # Se não existe essa estrada, retorna None (caminho inválido)
            return None
    return total

# Defina origem e destino (armazém → cliente)
origem = 'Armazem'
destino = 'CidadeC'

# Liste manualmente as rotas candidatas 
rotas_candidatas = [
    ['Armazem', 'CidadeA', 'CidadeC'],   # custo: 4 + 7 = 11
    ['Armazem', 'CidadeB', 'CidadeC'],   # custo: 6 + 3 = 9   (menor)
    ['Armazem', 'CidadeA', 'CidadeB', 'CidadeC'],  # 4 + 2 + 3 = 9  (empate)
]

# Calcular custos e escolher a menor
validas = []
for rota in rotas_candidatas:
    c = custo_caminho(G, rota)
    if c is not None:
        validas.append((rota, c))

# Mostrar resultados
print('--- Rotas candidatas e seus custos ---')
for rota, c in validas:
    print(f'{rota}  -> custo = {c}')

# Escolher a melhor (menor custo)
if validas:
    melhor_rota, melhor_custo = min(validas, key=lambda x: x[1])
    print('\nMENOR CAMINHO (manual):')
    print(f'Rota: {melhor_rota} | Custo total: {melhor_custo}')
else:
    print('Nenhuma rota candidata é válida.')

# =========================
# PARTE 3 — FALHA (remover estrada)
# =========================

# Simular falha de uma estrada importante (ex.: Armazem -> CidadeB)
falha = ('Armazem', 'CidadeB')
if G.has_edge(*falha):
    G.remove_edge(*falha)
    print(f'\n[AVISO] Falha simulada: estrada removida {falha}')
else:
    print(f'\n[INFO] Estrada {falha} não existia; nada removido.')

desenhar_grafo(G, 'Rede de Cidades após falha (uma estrada removida)')

# Recalcular os custos das mesmas rotas candidatas após a falha
validas_apos_falha = []
for rota in rotas_candidatas:
    c = custo_caminho(G, rota)
    if c is not None:
        validas_apos_falha.append((rota, c))

print('--- Rotas candidatas APÓS A FALHA ---')
if validas_apos_falha:
    for rota, c in validas_apos_falha:
        print(f'{rota}  -> custo = {c}')
    melhor2_rota, melhor2_custo = min(validas_apos_falha, key=lambda x: x[1])
    print('\nMENOR CAMINHO APÓS FALHA (manual):')
    print(f'Rota: {melhor2_rota} | Custo total: {melhor2_custo}')
else:
    print('Nenhuma rota permanece válida após a falha.')

# =========================
# PARTE 4 — ANÁLISE DE ROBUSTEZ (BÁSICA)
# =========================
print('\n[Robustez - ideia simples]')
print('- Estrada removida era crítica? Se o melhor caminho anterior usava essa estrada, o custo ou a rota mudou.')
print('- Compare a melhor rota antes e depois da falha (visual e pelos custos).')
print('- Se não restou nenhuma rota válida, a rede não é robusta para esse par de cidades.')
