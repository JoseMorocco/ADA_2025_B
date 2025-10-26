# Algoritmos.py

import heapq
import sys
import copy

inf = float('inf')

# --- Versiones con Pasos ---

# Dijkstra - Devuelve: (distancias, previous_nodes, pasos)
def dijkstra_con_pasos(grafo, inicio):

    vertices = grafo.obtener_vertices()
    distancias = {v: inf for v in vertices}
    previous_nodes = {v: None for v in vertices}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    processed_vertices = set()
    pasos_detallados = []

    pasos_detallados.append({
        'titulo': f"Paso 0: Estado Inicial (Inicio: {inicio})",
        'distancias': distancias.copy(), 'current_vertex': None,
        'processed_vertices': processed_vertices.copy(), 'relaxed_edges': []
    })

    while cola_prioridad:
        distancia_actual, u = heapq.heappop(cola_prioridad)
        
        if u in processed_vertices: continue
        processed_vertices.add(u)
        
        # Estado: Al procesar un nuevo nodo 'u'
        pasos_detallados.append({
            'titulo': f"Paso {len(pasos_detallados)}: Procesando Vértice {u} (Dist: {distancia_actual})",
            'distancias': distancias.copy(), 'current_vertex': u,
            'processed_vertices': processed_vertices.copy(), 'relaxed_edges': []
        })
        
        relaxed_edges_en_paso = []
        if u not in grafo.adj: continue # Vértice sin aristas salientes

        for v, peso in grafo.adj[u].items():
            if v not in processed_vertices:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[v]:
                    distancias[v] = nueva_distancia
                    previous_nodes[v] = u
                    heapq.heappush(cola_prioridad, (nueva_distancia, v))
                    relaxed_edges_en_paso.append((u, v)) # Guardar arista relajada
        
        if relaxed_edges_en_paso:
            # Estado: Después de relajar aristas desde 'u'
            pasos_detallados.append({
                'titulo': f"Paso {len(pasos_detallados)}: Relajando vecinos de {u} (Aristas en verde)",
                'distancias': distancias.copy(), 'current_vertex': u,
                'processed_vertices': processed_vertices.copy(),
                'relaxed_edges': relaxed_edges_en_paso
            })

    # Estado final
    pasos_detallados.append({
        'titulo': f"Paso Final: Algoritmo Completo",
        'distancias': distancias.copy(), 'current_vertex': None,
        'processed_vertices': processed_vertices.copy(), 'relaxed_edges': []
    })
    return distancias, previous_nodes, pasos_detallados

def reconstruir_camino_dijkstra(previous_nodes, inicio, fin):
    """Reconstruye el camino para Dijkstra."""
    camino = []
    actual = fin
    if previous_nodes[actual] is None and actual != inicio: return None 
    while actual is not None:
        camino.append(actual)
        actual = previous_nodes[actual]
    camino.reverse()
    return camino if camino[0] == inicio else None

# Floyd_warshall - Devuelve: (matriz_distancias, matriz_siguientes, pasos)
def floyd_warshall_con_pasos(grafo):
    pasos = []
    vertices = sorted(grafo.obtener_vertices())
    v_map = {v: i for i, v in enumerate(vertices)}
    inv_map = {i: v for i, v in enumerate(vertices)}
    n = len(vertices)
    
    dist = [[inf] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]
    
    for i in range(n): dist[i][i] = 0
        
    for u, v, peso in grafo.obtener_aristas(con_peso=True):
        i, j = v_map[u], v_map[v]
        dist[i][j] = peso
        next_node[i][j] = v # El siguiente nodo para ir de u a v es v
        if not grafo.adj[u].get(v) or not grafo.adj[v].get(u): # Asumir dirigido si no es simétrico
             if v in grafo.adj and u in grafo.adj[v] and grafo.adj[v][u] == peso:
                 dist[j][i] = peso
                 next_node[j][i] = u

    def convertir_matriz(d):
        m_final = {u: {} for u in vertices}
        for i in range(n):
            for j in range(n):
                m_final[inv_map[i]][inv_map[j]] = d[i][j]
        return m_final

    pasos.append({
        'titulo': "Paso 0: Matriz de Adyacencia Inicial",
        'k_vertex': None, 'distancias': convertir_matriz(dist), 'relaxed_edges': []
    })
    
    # Algoritmo principal
    for k_idx in range(n):
        k_vertex = inv_map[k_idx]
        relaxed_edges_en_paso = []
        for i_idx in range(n):
            for j_idx in range(n):
                dist_via_k = dist[i_idx][k_idx] + dist[k_idx][j_idx]
                if dist[i_idx][j_idx] > dist_via_k:
                    dist[i_idx][j_idx] = dist_via_k
                    next_node[i_idx][j_idx] = next_node[i_idx][k_idx]
                    relaxed_edges_en_paso.append((inv_map[i_idx], inv_map[j_idx])) # Arista (i,j)
        
        pasos.append({
            'titulo': f"Paso {k_idx + 1}: Usando '{k_vertex}' como intermediario",
            'k_vertex': k_vertex, 'distancias': convertir_matriz(dist),
            'relaxed_edges': relaxed_edges_en_paso
        })
            
    next_final = {u: {} for u in vertices}
    for i in range(n):
        for j in range(n):
            u, v = inv_map[i], inv_map[j]
            next_final[u][v] = next_node[i][j]
                
    return convertir_matriz(dist), next_final, pasos

def reconstruir_camino_floyd(next_node_matrix, u, v):
    if next_node_matrix[u][v] is None: return None
    camino = [u]
    actual = u
    while actual != v:
        siguiente = next_node_matrix[actual][v]
        if siguiente is None: return None # No hay camino
        actual = siguiente
        camino.append(actual)
    return camino

# Bellman Ford - Devuelve: (distancias, ciclo_negativo_encontrado, pasos)
def bellman_ford_con_pasos(grafo, inicio):
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas(con_peso=True)
    num_vertices = len(vertices)
    pasos = []
    
    distancias = {v: inf for v in vertices}
    previous_nodes = {v: None for v in vertices}
    distancias[inicio] = 0

    pasos.append({
        'titulo': f"Paso 0: Estado Inicial (Inicio: {inicio})",
        'distancias': distancias.copy(), 'relaxed_edges': []
    })

    # |V| - 1 relajaciones
    for i in range(num_vertices - 1):
        relaxed_edges_en_paso = []
        for u, v, peso in aristas:
            if distancias[u] != inf and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                previous_nodes[v] = u
                relaxed_edges_en_paso.append((u, v))
        
        if not relaxed_edges_en_paso: 
             break
        
        pasos.append({
            'titulo': f"Paso {i + 1}/{num_vertices - 1}: Relajación de aristas",
            'distancias': distancias.copy(), 'relaxed_edges': relaxed_edges_en_paso
        })

    # |V|-ésima relajación para encontrar un nodo en un ciclo negativo
    for u, v, peso in aristas:
        if distancias[u] != inf and distancias[u] + peso < distancias[v]:
            # ¡Ciclo negativo detectado!
            nodo_en_ciclo = v
            for _ in range(num_vertices):
                nodo_en_ciclo = previous_nodes[nodo_en_ciclo]
            
            ciclo = [nodo_en_ciclo]
            actual = previous_nodes[nodo_en_ciclo]
            while actual != nodo_en_ciclo:
                ciclo.append(actual)
                actual = previous_nodes[actual]
            ciclo.append(nodo_en_ciclo)
            ciclo.reverse()
            
            pasos.append({
                'titulo': f"Paso Final: ¡Ciclo Negativo Detectado!",
                'distancias': distancias.copy(), 'relaxed_edges': [], 'cycle_highlight': ciclo
            })
            return distancias, ciclo, pasos # Devuelve el ciclo
            
    pasos.append({
        'titulo': f"Paso Final: Algoritmo Completo (No hay ciclos)",
        'distancias': distancias.copy(), 'relaxed_edges': [], 'cycle_highlight': None
    })
    return distancias, None, pasos # No hay ciclo

# --- Versiones Simplificadas ---

def dijkstra_simple(grafo, inicio):
    distancias = {v: inf for v in grafo.obtener_vertices()}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    while cola_prioridad:
        distancia_actual, u = heapq.heappop(cola_prioridad)
        if distancia_actual > distancias[u]: continue
        if u not in grafo.adj: continue
        for v, peso in grafo.adj[u].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[v]:
                distancias[v] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, v))
    return distancias

def floyd_warshall_simple(grafo):
    vertices = grafo.obtener_vertices()
    dist = {u: {v: inf for v in vertices} for u in vertices}
    for u in vertices: dist[u][u] = 0
    for u in grafo.adj:
        for v, peso in grafo.adj[u].items():
            dist[u][v] = peso
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist_via_k = dist[i][k] + dist[k][j]
                if dist[i][j] > dist_via_k:
                    dist[i][j] = dist_via_k
    return dist

def bellman_ford_simple(grafo, inicio):
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas(con_peso=True)
    num_vertices = len(vertices)
    distancias = {v: inf for v in vertices}
    distancias[inicio] = 0
    
    for _ in range(num_vertices - 1):
        for u, v, peso in aristas:
            if distancias[u] != inf and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
    return distancias