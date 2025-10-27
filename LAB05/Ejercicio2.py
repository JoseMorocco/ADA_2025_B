from Grafo import Grafo
from Algoritmos import floyd_warshall_con_pasos, reconstruir_camino_floyd
import matplotlib.pyplot as plt

def imprimir_matriz(matriz):
    """Función auxiliar para imprimir la matriz de distancias."""
    vertices = sorted(matriz.keys())
    header = "     " + "  ".join(f"{v: >4}" for v in vertices)
    print(header)
    print("  " + "-" * (len(header) + 2))
    for u in vertices:
        fila = f"{u: <4} |"
        for v in vertices:
            dist = matriz[u][v]
            fila += f"{dist: >5.0f} " if dist != float('inf') else "   inf "
        print(fila)

def Ejercicio2():
    """
    Resuelve el Problema 2: Floyd-Warshall con visualización
    gráfica por cada nodo intermediario 'k'.
    """
    print("--- Problema 2: Algoritmo de Floyd-Warshall (Paso a Paso Gráfico) ---")
    
    # 1. Crear el grafo
    g = Grafo()
    num_vertices = 6
    num_aristas = 10 
    
    g.generar_aleatorio_letras(num_vertices, num_aristas, 
                               peso_min=1, peso_max=10, 
                               dirigido=True) 

    print(g)
    
    # 2. Calcular posiciones
    pos = g.get_nx_pos(dirigido=True) 
    print("="*50)

    # 3. Ejecutar Floyd-Warshall y obtener pasos
    matriz_distancias, matriz_siguientes, pasos = floyd_warshall_con_pasos(g)
    
    # 4. Mostrar los pasos 
    print("Visualizando los pasos del algoritmo (un gráfico por cada nodo 'k')...")
    
    for i, paso in enumerate(pasos):
        print(f"\n{paso['titulo']}")
        print("-" * len(paso['titulo']))
        
        imprimir_matriz(paso['distancias'])
        if paso['relaxed_edges']:
             print(f"Caminos actualizados en este paso: {len(paso['relaxed_edges'])}")
        
        g.dibujar_grafo_paso(pos, 
                             paso['titulo'], 
                             dirigido=True,
                             current_vertex=paso['k_vertex'], # Resaltar nodo 'k'
                             relaxed_edges=paso['relaxed_edges'] # Resaltar aristas (i, j)
                            )
        
        if i < len(pasos) - 1:
            print("\n>>> Cierra la ventana del gráfico para continuar al siguiente paso...")
            plt.show()
        else:
            print("\nAlgoritmo finalizado. Mostrando el último paso.")
            plt.show() 

    # 5. Mostrar resultados finales con caminos
    print("\n" + "="*50)
    print(f"--- Resultados Finales de Floyd-Warshall (Caminos) ---")
    vertices = sorted(g.obtener_vertices())
    for u in vertices:
        for v in vertices:
            if u == v: continue
            camino = reconstruir_camino_floyd(matriz_siguientes, u, v)
            dist = matriz_distancias[u][v]
            if camino:
                camino_str = " -> ".join(camino)
                print(f"Camino {u} -> {v}: {dist} (Camino: {camino_str})")
            else:
                print(f"Camino {u} -> {v}: {dist} (No hay camino)")

if __name__ == "__main__":
    Ejercicio2()