# Grafo.py

import random
import networkx as nx
import matplotlib.pyplot as plt 

class Grafo:
    
    def __init__(self):
        self.adj = {}
        self.vertices = set()

    def agregar_vertice(self, vertice):
        if vertice not in self.adj:
            self.adj[vertice] = {}
            self.vertices.add(vertice)

    def agregar_arista(self, u, v, peso, dirigido=False):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adj[u][v] = peso
        if not dirigido:
            self.adj[v][u] = peso

    def obtener_peso(self, u, v):
        return self.adj.get(u, {}).get(v, float('inf'))

    def obtener_vertices(self):
        return list(self.vertices)

    def obtener_aristas(self, con_peso=True):

        aristas = []
        for u in self.adj:
            for v, peso in self.adj[u].items():
                aristas.append((u, v, peso) if con_peso else (u, v))
        return aristas

    def generar_aleatorio(self, num_vertices, num_aristas, peso_min=1, peso_max=10, dirigido=False):
        """Genera grafo aleatorio con vértices numéricos (para Problema 4)."""
        self.adj = {}
        self.vertices = set()
        for i in range(num_vertices):
            self.agregar_vertice(i)
        
        aristas_creadas = set()
        max_aristas = num_vertices * (num_vertices - 1)
        if num_aristas > max_aristas: num_aristas = max_aristas
             
        while len(aristas_creadas) < num_aristas:
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
            if u == v or (u, v) in aristas_creadas: continue
            
            peso = random.randint(peso_min, peso_max)
            self.agregar_arista(u, v, peso, dirigido=dirigido)
            aristas_creadas.add((u, v))
            if not dirigido: aristas_creadas.add((v, u))

    def generar_aleatorio_letras(self, num_vertices, num_aristas, peso_min=1, peso_max=10, dirigido=False):
        """Genera grafo aleatorio con vértices de letras (para Problemas 1, 2, 3)."""
        self.adj = {}
        self.vertices = set()
        
        nombres_vertices = [chr(65 + i) for i in range(num_vertices)]
        for v_nombre in nombres_vertices:
            self.agregar_vertice(v_nombre)
        
        aristas_creadas = set()
        max_aristas = num_vertices * (num_vertices - 1)
        if num_aristas > max_aristas: num_aristas = max_aristas

        while len(aristas_creadas) < num_aristas:
            u = random.choice(nombres_vertices)
            v = random.choice(nombres_vertices)
            if u == v or (u, v) in aristas_creadas: continue
                
            peso = random.randint(peso_min, peso_max)
            self.agregar_arista(u, v, peso, dirigido=dirigido)
            aristas_creadas.add((u, v))
            if not dirigido: aristas_creadas.add((v, u))

    def __str__(self):
        s = "Grafo (Lista de Adyacencia):\n"
        for u in sorted(self.adj.keys()): 
            s += f"  {u}: {self.adj[u]}\n"
        return s

    def get_nx_pos(self, dirigido=False, seed=42):
        """Calcula y devuelve la posición de los nodos para NetworkX."""
        G = nx.DiGraph() if dirigido else nx.Graph()
        G.add_nodes_from(self.vertices)
        
        edges_for_layout = []
        if dirigido:
            # Para DiGraph, solo queremos las aristas (u, v)
            edges_for_layout = self.obtener_aristas(con_peso=False)
        else:
            # Para Graph, necesitamos evitar duplicados en el layout
            temp_edges = set()
            for u, v in self.obtener_aristas(con_peso=False):
                if (u,v) not in temp_edges and (v,u) not in temp_edges:
                    temp_edges.add((u,v))
            edges_for_layout = list(temp_edges)
            
        G.add_edges_from(edges_for_layout)
        
        return nx.spring_layout(G, k=0.9, seed=seed)

    def dibujar_grafo_paso(self, pos, titulo, dirigido=False, **kwargs):
        """Dibuja un estado específico del algoritmo."""
        G = nx.DiGraph() if dirigido else nx.Graph()
        G.add_nodes_from(self.vertices)
        
        edge_labels = {}
        all_edges = []
        
        # Usamos la función corregida
        for u, v, peso in self.obtener_aristas(con_peso=True):
            if not G.has_edge(u, v):
                G.add_edge(u, v, weight=peso)
                all_edges.append((u, v))
                edge_labels[(u, v)] = peso
            # Si no es dirigido, nos aseguramos que networkx tenga ambas direcciones
            if not dirigido:
                 if not G.has_edge(v, u):
                    G.add_edge(v, u, weight=peso)
                    all_edges.append((v, u))
                    edge_labels[(v, u)] = peso


        plt.figure(figsize=(12, 8))
        
        # 1. Colores de Nodos
        node_colors = []
        processed = kwargs.get('processed_vertices', set())
        current = kwargs.get('current_vertex')
        path = kwargs.get('path_highlight', [])
        # Esta corrección (que ya tenías) es para evitar el error con None
        cycle = kwargs.get('cycle_highlight') or [] 
        
        for node in G.nodes():
            if node == current:
                node_colors.append('red') # Nodo actual
            elif node in cycle:
                node_colors.append('darkorange') # Ciclo
            elif node in path:
                node_colors.append('salmon') # Camino
            elif node in processed:
                node_colors.append('skyblue') # Procesado
            else:
                node_colors.append('lightgray') # No visitado
        
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_colors, alpha=0.9)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

        # 2. Colores de Aristas
        edge_colors = []
        edge_widths = []
        relaxed = kwargs.get('relaxed_edges', [])
        path_edges = list(zip(path, path[1:])) if path else []
        cycle_edges = list(zip(cycle, cycle[1:])) if cycle else []
        
        # Iteramos sobre las aristas que networkx va a dibujar
        for u, v in G.edges():
            if (u, v) in cycle_edges or (v, u) in cycle_edges:
                edge_colors.append('darkorange')
                edge_widths.append(3.0)
            elif (u, v) in path_edges or (v, u) in path_edges:
                edge_colors.append('red')
                edge_widths.append(3.0)
            elif (u, v) in relaxed or (v, u) in relaxed:
                edge_colors.append('green') 
                edge_widths.append(2.5)
            else:
                edge_colors.append('gray')
                edge_widths.append(1.0)

        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=edge_colors, 
                               width=edge_widths, alpha=0.6, arrows=dirigido, 
                               arrowstyle='->', arrowsize=15)
        
        # 3. Etiquetas de Peso
        # Hacemos coincidir las etiquetas con las aristas que networkx tiene
        final_edge_labels = {}
        for u, v in G.edges():
            if (u,v) in edge_labels:
                final_edge_labels[(u,v)] = edge_labels[(u,v)]
            elif (v,u) in edge_labels and not dirigido:
                final_edge_labels[(u,v)] = edge_labels[(v,u)]
                
        nx.draw_networkx_edge_labels(G, pos, edge_labels=final_edge_labels, font_size=10)
        
        plt.title(titulo, fontsize=16)
        plt.axis('off')