import random
from Grafo import Grafo
from Algoritmos import dijkstra_con_pasos, reconstruir_camino_dijkstra
import matplotlib.pyplot as plt

def Ejercicio1():
    print("--- Problema 1: Algoritmo de Dijkstra ---")
    
    # 1. Crear el grafo
    g = Grafo()
    num_vertices = 8  
    num_aristas = 15
    g.generar_aleatorio_letras(num_vertices, num_aristas, 
                               peso_min=1, peso_max=10, 
                               dirigido=False)

    print(g) 

    # 2. Definir inicio y calcular posiciones
    vertice_inicio = random.choice(g.obtener_vertices())
    pos = g.get_nx_pos(dirigido=False)
    print(f"Calculando el camino más corto desde: {vertice_inicio}\n")
    print("="*50)

    # 3. Ejecutar Dijkstra y obtener pasos
    distancias, previous_nodes, pasos = dijkstra_con_pasos(g, vertice_inicio)
    
    # 4. Mostrar los pasos 
    print("Visualizando los pasos del algoritmo...")
    
    for i, paso in enumerate(pasos):
        print(f"\n{paso['titulo']}")
        print("-" * len(paso['titulo']))
        
        # Imprimir distancias actuales en texto
        dist_str = ", ".join(
            f"{v}: {d if d != float('inf') else '∞'}" 
            for v, d in sorted(paso['distancias'].items())
        )
        print(f"Distancias: {dist_str}")
        print(f"Procesados: {paso['processed_vertices']}")
        
        # Generar el gráfico para este paso
        g.dibujar_grafo_paso(pos, 
                             paso['titulo'], 
                             dirigido=False,
                             current_vertex=paso['current_vertex'],
                             processed_vertices=paso['processed_vertices'],
                             relaxed_edges=paso['relaxed_edges']
                            )
        
        if i < len(pasos) - 1:
            print("\n>>> Cierra la ventana del gráfico para continuar al siguiente paso...")
            plt.show()
        else:
            print("\nAlgoritmo finalizado. Mostrando el último paso.")
            plt.show() 

    # 5. Mostrar resultados finales
    print("\n" + "="*50)
    print(f"--- Resultados Finales de Dijkstra (Inicio: {vertice_inicio}) ---")
    
    for v in sorted(g.obtener_vertices()):
        dist = distancias[v]
        camino = reconstruir_camino_dijkstra(previous_nodes, vertice_inicio, v)
        
        if camino:
            camino_str = " -> ".join(camino)
            print(f"Camino a {v}: {dist} (Camino: {camino_str})")
        else:
            print(f"Camino a {v}: {dist} (No hay camino)")

    # 6. Dibujar el grafo final 
    vertice_ejemplo = None
    caminos_validos = [v for v in g.obtener_vertices() if v != vertice_inicio and distancias[v] != float('inf')]
    if caminos_validos:
        vertice_ejemplo = random.choice(caminos_validos)
        
    if vertice_ejemplo:
        camino_final = reconstruir_camino_dijkstra(previous_nodes, vertice_inicio, vertice_ejemplo)
        titulo_final = f"Camino más Corto de {vertice_inicio} a {vertice_ejemplo} (Costo: {distancias[vertice_ejemplo]})"
        print(f"\nMostrando un camino de ejemplo: {titulo_final}")
        g.dibujar_grafo_paso(pos, titulo_final, dirigido=False, 
                             processed_vertices=g.obtener_vertices(),
                             path_highlight=camino_final)
        print("\n>>> Cierra la ventana del gráfico para terminar.")
        plt.show() 
    else:
        print("\nNo se encontraron caminos para mostrar un ejemplo.")

if __name__ == "__main__":
    Ejercicio1()