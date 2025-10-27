import time
import csv
from Grafo import Grafo
# Importamos las versiones simples para velocidad
from Algoritmos import dijkstra_simple, bellman_ford_simple, floyd_warshall_simple

def medir_tiempos():

    TAMANOS = [
        (10, 20), (20, 80), (50, 250), (80, 800),
        (100, 1500), (150, 3000), (200, 5000) 
    ]
    
    resultados = []
    
    print("Midiendo tiempos... (esto puede tardar unos segundos)")
    print("-" * 70)
    print(f"{'Vértices (V)': <12} | {'Aristas (E)': <12} | {'Dijkstra (s)': <15} | {'Bellman-Ford (s)': <15} | {'Floyd-Warshall (s)': <18}")
    print("-" * 70)

    for v, e in TAMANOS:
        # 1. Generar grafo 
        g = Grafo()
        g.generar_aleatorio(v, e, peso_min=1, peso_max=100, dirigido=True)
        inicio = 0 # Vértice de inicio estándar 0
        
        # 2. Medir Dijkstra (simple)
        t_inicio = time.perf_counter()
        dijkstra_simple(g, inicio)
        t_dijkstra = time.perf_counter() - t_inicio
        
        # 3. Medir Bellman-Ford (simple)
        t_inicio = time.perf_counter()
        bellman_ford_simple(g, inicio)
        t_bellman = time.perf_counter() - t_inicio
        
        # 4. Medir Floyd-Warshall (simple)
        t_inicio = time.perf_counter()
        floyd_warshall_simple(g)
        t_floyd = time.perf_counter() - t_inicio
        
        # 5. Guardar y mostrar resultados
        resultados.append([v, e, t_dijkstra, t_bellman, t_floyd])
        print(f"{v: <12} | {e: <12} | {t_dijkstra: <15.6f} | {t_bellman: <15.6f} | {t_floyd: <18.6f}")

    # 6. Escribir resultados a un archivo CSV para Problema 5
    nombre_archivo = "tiempos.csv"
    try:
        with open(nombre_archivo, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['V', 'E', 'Dijkstra', 'BellmanFord', 'FloydWarshall'])
            writer.writerows(resultados)
        print(f"\nResultados guardados en '{nombre_archivo}' para usar en Problema 5.")
    except IOError as err:
        print(f"\nError al guardar el archivo CSV: {err}")

if __name__ == "__main__":
    medir_tiempos()